# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWZWTQKO4K"
aws_secret_access_key="rPTFOgdxrCwIeDvmbAR9VxMBeUizLV1nEGBzXVNR"
aws_session_token="FwoGZXIvYXdzEEEaDOGLh9QhKCNjjSrs+iLAAb7I8DJgaDgljCekHl5VL/mPMllMzA2/2tcWg2OY9OjMt4ThN86FzI5Nj8Wfu+NVWVKRj/EBi7qDMkkSkHowT5tROoqkCPnmmd2iGJbm7C77g4cGFZN7g1A9Nvr3VsQfMnk3ZpZ+7mp2A6MdUYUyNDXX6p+PUDgXlgilxsLZKzGFMEMr//IcuP3UDPkUGkvsCzYqAmqIHWjc68JUWxeopdHJ8w4Xltd3wuqd+Ja9iKzBu89p68ZeeAPUKyxyLqVywSjlkbiWBjIt3XP6GkRm3BAzWKvGml6NSgarlXLnIj/a/ynzNsBHMB1mlJfBzLBxMDEdc7cp"
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
get_doc = "http://44.201.70.102/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"