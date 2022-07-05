import time
import pickle
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
        import pdb; pdb.set_trace()
        return jsonify(result), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)