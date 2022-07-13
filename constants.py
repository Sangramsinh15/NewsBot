# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWZWTQKO4K"
aws_secret_access_key="rPTFOgdxrCwIeDvmbAR9VxMBeUizLV1nEGBzXVNR"
aws_session_token="FwoGZXIvYXdzEEEaDOGLh9QhKCNjjSrs+iLAAb7I8DJgaDgljCekHl5VL/mPMllMzA2/2tcWg2OY9OjMt4ThN86FzI5Nj8Wfu+NVWVKRj/EBi7qDMkkSkHowT5tROoqkCPnmmd2iGJbm7C77g4cGFZN7g1A9Nvr3VsQfMnk3ZpZ+7mp2A6MdUYUyNDXX6p+PUDgXlgilxsLZKzGFMEMr//IcuP3UDPkUGkvsCzYqAmqIHWjc68JUWxeopdHJ8w4Xltd3wuqd+Ja9iKzBu89p68ZeeAPUKyxyLqVywSjlkbiWBjIt3XP6GkRm3BAzWKvGml6NSgarlXLnIj/a/ynzNsBHMB1mlJfBzLBxMDEdc7cp"

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
get_doc = "http://44.201.70.102/get_relevant_docs"