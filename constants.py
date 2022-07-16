# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWV5DVFY74"
aws_secret_access_key="arMWmG1OV8p1MuSPkdgHQoQEpZ7Py5srnkhHuLNC"
aws_session_token="FwoGZXIvYXdzEJb//////////wEaDDkzSr1ik/FcBmYjtiLAAShjmCLJvZzEghg4BJjUiXXM+WgvuRIGKclk4i+pF/qDApyzdnl3+9ftcjpcIFuxrLBVFL33/x/knww3oQH56cuemiTTRcDi0fAvxEobqIRAzNP+A1xGzSjyjpMP9FwDQtU8f0kAngyWeoiSdOntnyMP59eHxo3TT/1Yhr2jkLYP9DSo8ynMWG0kH5I5oKVc6yVcH17qqMGwk+TMefoOvDEwsId70PqbUp4JIEpgw3g1zYEwh41D6clXFHYmAQBoJCjb5MqWBjIt72EEFTFUjDwJbTL3B+dSjEkX1cfkvjengKh6/ohTK06piR2aA55En3E4JpYH"
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
get_doc = "http://3.239.94.21/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
