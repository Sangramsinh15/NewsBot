# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWRSHWTBVX"
aws_secret_access_key="jRs/GT2H8vOJ6WSb0awTumIMhMRDN1+m6R0UQviM"
aws_session_token="FwoGZXIvYXdzEE4aDJJmvy1ckoJW3HjvZCLAAZETFdj+X+qqDwCp7cgAlLivm4kbFfrKUO2O/voMVqINYVdC6TypkSl6D9REgED9vVc+b1RFnoRT7BxH2cmYpp2gADk2aPUuihg4AD4aQFsQxHSmhH070WBiCb7jcS4Jaampb9mHdFNrrAcDrxyRPIRpcLcw9aGEPX2sPIyWQTM0O3K391DGhzK1bGUM1Z1eGAXJDi1RZ0MZQOk03rCrI7zkPo6HYjDSimE798+v9+3USnwea5QHu9TKJMjyfj2vbijQ9LqWBjItIi4Fw47MWhGtRsICgoTcWZipuEHU00ZLX4uC5atLvNYGKwczcjse1+WNGQ/U"
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
get_doc = "http://34.231.244.174/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
