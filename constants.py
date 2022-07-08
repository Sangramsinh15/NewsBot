# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWRK4KHKKB"
aws_secret_access_key="U2tIvO0EOWYK1RzNoN8hHIELaepEDPBjLjQzL1/h"
aws_session_token="FwoGZXIvYXdzEM3//////////wEaDHBbd1fP9lVMAFORxiLAAX9UWoDriyIORQ/grOV7cIawoHwhK6NXNldGc/S3RBVmgSDG4nDWD1OFsmCHYcObAcyUmtP0I8Blg/Wms9uphHC0Ppl4132pZcSE7OnFDy671Xi5Yk9VZScLu572c3QN2mtb/gkSfrL8JYmktvGRVLCyN4s0CrEzcrrWtcUHsom/BR6owmQ+J+QebwGaAz+mMMs6Jlrrb8vz1rTV4abfSrXoNS0io7cG/ZgDFvZ8SZRIqIPRHNvavDNJSCoMr6UO9Cjmz56WBjItvvgl9Y29eqcDtgBchY5YLiOkDhEQzq/29+Vh8m66aSQ4mjMdxRz16jpdobDN"

# For Crawlers
bucket_name = "crawled-unprocessed-data"

# For Model Creation and Deployment
model_output_folder = "./model/"
model_file_name = "rss_model.pkl"
corpus_file_name = "corpus.pkl"
metadata_file_name = "metadata.pkl"
top_document_count = 5

# Dynamo-DB Details
table_name = "news_data"

# APIs
get_doc = "http://18.233.156.42/get_relevant_docs"