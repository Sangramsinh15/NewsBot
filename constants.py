# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCW6GASM64I"
aws_secret_access_key="mnPCe2bTzkaA4FneunJCI9XjHbsnAQt6om0wm/ve"
aws_session_token="FwoGZXIvYXdzELP//////////wEaDGUIF+UMZIFWFiOKMiLAAb9sfhrQrZRrqN4jsKqz3OjVHDT74G/8tkb3ujS6lLDTMox4xXdG0y4xbu69HjGzzNzKkBB5FOq1RLqdPj7uxty0etNohqeHkccL/z05rl8LbP8RRwtwZHCRuliRBJV4vXprAOHgtZ6B/MktEE7W2IKMvOCYOX712yEchPy1ZU2R/dTlUsd5dkyON0tp21P2UW+OJT2DiLFzTBQCN7VenZ7FmgvUlxC8KukbpNBKPd06C/2InCsIU+NbO4K/0Xk/qCiJltGWBjItivWXufXkm73lhqpA+ImMZI5GCVOEJv0eeqLjGEjz07krpUgJMZEdSc+kqaT7"
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
get_doc = "http://3.237.3.159/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"
