# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWRSHWTBVX"
aws_secret_access_key="jRs/GT2H8vOJ6WSb0awTumIMhMRDN1+m6R0UQviM"
aws_session_token="FwoGZXIvYXdzEE4aDJJmvy1ckoJW3HjvZCLAAZETFdj+X+qqDwCp7cgAlLivm4kbFfrKUO2O/voMVqINYVdC6TypkSl6D9REgED9vVc+b1RFnoRT7BxH2cmYpp2gADk2aPUuihg4AD4aQFsQxHSmhH070WBiCb7jcS4Jaampb9mHdFNrrAcDrxyRPIRpcLcw9aGEPX2sPIyWQTM0O3K391DGhzK1bGUM1Z1eGAXJDi1RZ0MZQOk03rCrI7zkPo6HYjDSimE798+v9+3USnwea5QHu9TKJMjyfj2vbijQ9LqWBjItIi4Fw47MWhGtRsICgoTcWZipuEHU00ZLX4uC5atLvNYGKwczcjse1+WNGQ/U"

# Redis
redis_ttl = 20*60  #20 minutes

# Lex
lex_api = "https://runtime.lex.us-east-1.amazonaws.com/bot/NewsBotOne/alias/NOneTester/user/user2030182/text"
lex_header = {
  'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
  'X-Amz-Security-Token': 'FwoGZXIvYXdzED0aDDhmYqgqj/ofr7P0IyLAAQx0verb8P6FX98Osj6/MCt6yE4syVcAi8LxStQspGRCGfk4YCp2u+VZmHqMAYS3yks+UZSVq5PoBtf36hxAc36PcjAZV4PfhaEwN44KyrGZK++zCnuFiShnA73KHGoVp4JFNED3d3TP/fWZnDOxz81Q4mSW+4ENMms3b+ycsvpJCRHQzvNT+Cpal96z+lHHj2mhcrnMCp2c1thb9824ohe6Mc5UolKAX2GpkAWA7ws0ImsA5yqFWjUfXkKpqFJYhij6preWBjItAMGY62a8VRm1bxXp9Ib3J9qmAeVNBCQu10oZOFiZDRsTZwzHmy7eG5YYoV+4',
  'X-Amz-Date': '20220712T201837Z',
  'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAX5UJGMCWZ7FRPOIL/20220712/us-east-1/lex/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=0cb249cad0a3948f6fd529da153efe6bcf75858903c461aa8660eae549be3a3e',
  'Content-Type': 'application/json'
}

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