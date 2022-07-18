# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWZPYQ6RJO"
aws_secret_access_key="vNq7hxvdsEgIJTdn1UPUEu8ckW7CL1zlNTcGcmSV"
aws_session_token="FwoGZXIvYXdzEMT//////////wEaDCz16OM9m5bgGmPkACLAASVgGjg88+8n0KN5MoxrpVc39HTquvrqpuxVFqE59hT6NxuLET6BLFu+vqre1dLG3F3gsgoVL/KBYmXMrfdLIsmq/gq3iS/igCCchNL5TPoAzoMPLkN9GQipNGHnr7IsxbaS4JMFgoaMjFN0kUG6XgC7vnI4lewoEuFhxBOPdI6VNjAfzxBnsGsKMKrT3xc2LKC5cCxXG6sYaqoyYLGvg9oC03PLT/5l7qzLNShrCqJQl3F+TkyCHRoSiOUUiv0Uxiit+9SWBjIt4AdgbyiCCGs4d1rQ1ahXbyrp4S5M6DT3UgHfn8wYkamo0iuvhFg8U9u/vWl5"
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
get_doc = "http://34.239.166.42/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"