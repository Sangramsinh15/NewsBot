# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCW2BW4MI5D"
aws_secret_access_key="NDueB46lNnLMc2/EJKzKmi8z4ClSWEUclD+gB8fa"
aws_session_token="FwoGZXIvYXdzEMf//////////wEaDH+WaxkE216yEdVXOyLAAXdOc2cBgqqwgyA0QjxVZq4DzxmQ+zpbLIR6nO7dKw+TtGRiwi+4XHqTN63Hw3F7j08zEvsGXuHtAj2yPZ54WbxBricpDOC+3A5sfisNdqo/V/W2raLrbAgxj48x9ZOvUQcZs02vkA0WPhCCjd3HzYvKYfvDpJHNqavFTjePsUGE9Pvt3cCm3W3EZZTz3uTjiJWp2weEuAB3uL0a2NCUW7JMcuBDEyQmV+Yuk041TRnLSa638AP3zzA9zaK4sdPDciiimZ2WBjItceuTPpQOogfclIVJHfdpyx+kDP3J75TNybDd4gtzw1wzQ63dpPJDr40RqyrS"

# For Crawlers
bucket_name = "crawled-unprocessed-data"

# For Model Creation and Deployment
model_output_folder = "./model/"
model_file_name = "rss_model.pkl"
corpus_file_name = "corpus.pkl"
metadata_file_name = "metadata.pkl"
top_document_count = 5

# Dynamo-DB Details
table_name = "news_data"

# APIs
get_doc = "http://18.233.156.42/get_relevant_docs"