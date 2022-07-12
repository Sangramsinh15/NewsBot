import pdb
import random
import time
import json
import redis
import pickle
import traceback

import requests
from flask import Flask, request, jsonify
from sentence_transformers import SentenceTransformer

import constants
from train_model import TrainModel
from test_model import TestModel
from s3Utilities import S3Utilities
from dynamoUtilities import DynamoUtilities

app = Flask(__name__)
s3_obj = S3Utilities(access_key_id=constants.aws_access_key_id, secret_access_key=constants.aws_secret_access_key, session_key=constants.aws_session_token)
dynamo_obj = DynamoUtilities(access_key_id=constants.aws_access_key_id, secret_access_key=constants.aws_secret_access_key, session_key=constants.aws_session_token)
redis_obj = redis.Redis(host= 'localhost', port= 6379)
redis_obj.flushall()

embeddings, metadata, embedder = None, None, None
with open(constants.model_output_folder + constants.model_file_name, "rb") as fp:
    ip_embeddings = pickle.load(fp)
    embeddings = ip_embeddings["embeddings"]
    metadata = ip_embeddings["metadata"]
embedder = SentenceTransformer('all-MiniLM-L6-v2')

@app.route("/train_updated_data", methods=['POST'])
def initiate_training():
    st = time.time()
    TrainModel().main()
    return jsonify({"message": "Model successfully trained in {0} seconds. Restart the service in the server to load the new model!".format(int(time.time() - st))}), 200

@app.route("/get_relevant_docs", methods=["GET"])
def get_relevant_data():
    jsonPayload = request.get_json()
    text = jsonPayload.get("text", None)
    if not text:
        return jsonify({"message": "Send 'text' parameter in body"}), 400
    else:
        result = TestModel().test(metadata, embeddings, text, embedder, constants.top_document_count)
        return jsonify(result), 200

@app.route("/get_response_1", methods=["GET"])
def get_response_1():
    jsonPayload = request.get_json()
    text = jsonPayload.get("text", None)
    session_id = jsonPayload.get("session_id", None)
    if not text:
        return jsonify({"message": "Send 'text' parameter in body"}), 400
    if not session_id:
        return jsonify({"message": "Send 'session_id' parameter in body"}), 400
    else:
        resp = get_response_from_lex(text)

        if resp is None or resp == "Abra Ka Dabra":
            if resp is None:
                print("No response from Lex")
            elif resp == "Abra Ka Dabra":
                print("Got default response from Lex")
            result = TestModel().test(metadata, embeddings, text, embedder, constants.top_document_count)
            tags = list(set([each["source_tag"] for each in result]))
            if len(tags)>1:
                redis_obj.set(session_id, json.dumps(result), constants.redis_ttl)
                m = random.choice(["Found some articles, on which genre?", "Ammmm..! Which one?", "I am confused :/ On which genre?"])
                return jsonify({"message": m, "hidden_message": True, "tags": tags, "data_to_display": None}), 200
            else:
                m = random.choice(["Found something..", "Voila..!", "Bingo.!.", "I hope you like these.."])
                return jsonify({"message": m, "hidden_message": None, "tags": [], "data_to_display": result}), 200
        else:
            return jsonify({"message": resp, "hidden_message": None, "tags": [], "data_to_display": None}), 200

@app.route("/get_response_2", methods=["GET"])
def get_response_2():
    jsonPayload = request.get_json()
    text = jsonPayload.get("text", None)
    session_id = jsonPayload.get("session_id", None)
    if not text:
        return jsonify({"message": "Send 'text' parameter in body. This will be the tag that you will fetch from the user."}), 400
    if not session_id:
        return jsonify({"message": "Send 'session_id' parameter in body. This session_id will be the same that you have already sent in get_response_1."}), 400
    else:
        redis_data = redis_obj.get(session_id)
        if redis_data:
            redis_data = json.loads(redis_data)
            data_to_return = [each for each in redis_data if each["source_tag"]==text]
            if data_to_return:
                m = random.choice(["Found something..", "Voila..!", "Bingo.!.", "I hope you like these.."])
            else:
                data_to_return = redis_data
                m = random.choice(["Ahhh..there you go!", "I think you meant all..", "Okay okay got it, just have a look at these.."])
            redis_obj.delete(session_id)
            return jsonify({"message": m, "hidden_message": None, "tags": [], "data_to_display": data_to_return}), 200

def get_response_from_lex(text):
    result = None
    try:
        result = "Abra Ka Dabra"
        # resp = requests.post(constants.lex_api, headers=constants.lex_header, data=json.dumps({"inputText": text}))
        # if resp.status_code == 200:
    except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
