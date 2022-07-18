# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWW2RH6JP2"
aws_secret_access_key="8oDzA7Jj5UAfbRO1umeqls1wDJRM3mGeYcZ1b77n"
aws_session_token="FwoGZXIvYXdzEL3//////////wEaDK8kHfKEVQbSFCkAPSLAAcWgfulY/MwwK1/1qlJ7XggpJJjzks77WtL0LzE3kbRm/V66OZtfCQXULQOON00UFTPxHKLVoe90QK4TXzkSaZfQWf07tp11GxfGjD9ia40APFmSnbRD6k0lF/tO1FZkUvs4YUuK5rLfOPxmWZz9PJuswU9er7jfjY1+L/NSj56rwIeIZefkOVUGIMTOh1uV9NsrC+4oB6FDiUuwozH3uN8Y2wcMrjA5e+zs+RoMwU5c23Sb+u+eH7kObqQoBn7OoSjGsdOWBjIt7vw46p4x6/FN08Ca0uUoUm2CSLTGvdOb0mrH2ywP1tLNQeyQrY8vpYhgS8nu"
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
get_doc = "http://44.192.74.183/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"