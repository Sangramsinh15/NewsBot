# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWTKEZI3OO"
aws_secret_access_key="Uh7qFkBpgqffCJ3oSjqeyJPjtmM4YOdU/1vky36W"
aws_session_token="FwoGZXIvYXdzEFIaDOEB8onLe5tWodHysiLAAavMHYJFFqXN26pnDl/gcChcodZZA97gRMZgv7CFklxBvWAx9aiGTUltq6NqG7yOMtK3+V3OLwrgl+UM0BIe3oV7ZD0WX1hhcjEc/E+oEdtZNZmngdO79dtLf0WTyroUCwwykl1hNqnCPjw+PyuSR5QlHvez6kUZxYCKue4UJ64d0yF9pHsBiNhwg6TH8OzWEEl+DumXgvSsDSPmLl3tyMJ97ImkfNLiYI4zBEfda2tl5nucGwYm717AGxKra57j4Cjk5buWBjItPyFFTAFDAMGBRfhTvGTyebrJmxcwJtYL5Q5Rw4uM0iD9eU9W2TjXSOhoyV1c"
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
get_doc = "http://3.237.3.19/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
