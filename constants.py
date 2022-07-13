# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWQKMBDPG4"
aws_secret_access_key="gqvREsU2Dzs9qI+yITXAlmATMV+sh0+oOjQ5Iv3X"
aws_session_token="FwoGZXIvYXdzEFYaDALM/gjYqHKqBiXb6iLAAWBt+ITHPQRQnCV+YAI4YuzRGITWEg808f6CKkXdj2940zcrlwE9aedTLRvPHsmEK7XfBq6Wf+6rGJ0wK+SQh+zVxbHc7fRgxIBqmf1ObXgorFqDHmEEAsyQYoO9hwGWBidDp5AO/k4eAx7yqkm3FSjkfIY00tay8lO6kbMmMgIJZf7k6afdA0ApCSbhm2hs+JbPAmZ7bjIRFfgsqie6UpsHClVbdEzlqoz4Edmk1CMV6V3xzzob4VfZcC+2gF6xEyiX1byWBjIt+qJhwmQLm593F211/jvlsYk7/SvJX4D4Qty2pt+L/SuVPqDnn3UrUrVFU4fm"
aws_userId="user2027430"

# Redis
redis_ttl = 20*60  #20 minutes

# For Crawlers
bucket_name = "crawled-unprocessed-data"

# For Model Creation and Deployment
model_output_folder = "./model/"
model_file_name = "rss_model.pkl"
corpus_file_name = "corpus.pkl"
metadata_file_name = "metadata.pkl"
top_document_count = 5

# Dynamo-DB Detailsce
table_name = "news_data"

# APIs
get_doc = "http://3.235.31.252/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
