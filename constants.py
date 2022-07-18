# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCW6GFMWQZJ"
aws_secret_access_key="LCD5dunVBpk6bHXRAjQbx11qGDVIcHIyaV2yrSjz"
aws_session_token="FwoGZXIvYXdzEMj//////////wEaDKu13aGbKjgqBg7uByLAAW4w+eeEvexLuqdGQLN+Rn/1bEqZWXr5E5DB4HifMaH/48vB3sfk2f6apcmfVWyl48Vy1fjVGMxH4B7hlK+aDnzZ54BP4/5+8RI4ernyaI28kJOeQqUXTK+8I4+FEsIT3bl90OQwNs6VOIvFD4K/pftqqEIP3U9zmNs/hE+cs7ITPXzKCnlDvBAmde1AjmCONIRx9lK/ri4xrCImyhPphIZ2/XZDREm1MIvH/9qWPKlUb6Hn6Ew7NVyNrdT/i8ohFCil4tWWBjItyYdOXJwhpF0m5V4pfGMLTAenxDwhelNb6DU0ru3sYalv9Iv2HzvYzsZjZzqY"
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
get_doc = "http://100.24.117.242/get_relevant_docs"

# Lex
botName="NewsBotOne"
botAlias="TestBotOP"