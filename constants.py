# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWVYY6WOGX"
aws_secret_access_key="Hm7Se82qvekeEbTBArcuBB+EhxLD2WtR8N0Snhnm"
aws_session_token="FwoGZXIvYXdzELf//////////wEaDNqJkykqQkzUyGa6TiLAASmLJeuhWBgr4rcMwJJ7UttKCSUyyQPblAtb9TpaSU/vt4/w+nWBi+dMSOgN8aR23g11ZMojkMZ3bYadE1rvl3wOb3lBM/0DEs+Wz6zcEoVQzKpRET6VX1v/4TbU9xE6Rx0wt9QyI9mTr3/AwJ1jTU5VAzTzXakvRvBAt6F47nHbjf7FlMQncvbGMvY1uvOIh4vY/AtTcIf8wpyRtr6V/Fy3ZYJWCg2PPwJC5ow9reSigII/XcIHCNys4RfAISY9ASiIhNKWBjItMmYsb4qbslxa+q/1HHC/ZiNEbBhViiGpcI4fkyqDOZ6r9biykPk6VmSFxWm3"
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
get_doc = "http://3.235.66.246/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"