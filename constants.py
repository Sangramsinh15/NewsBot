# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCWRK4KHKKB"
aws_secret_access_key="U2tIvO0EOWYK1RzNoN8hHIELaepEDPBjLjQzL1/h"
aws_session_token="FwoGZXIvYXdzEM3//////////wEaDHBbd1fP9lVMAFORxiLAAX9UWoDriyIORQ/grOV7cIawoHwhK6NXNldGc/S3RBVmgSDG4nDWD1OFsmCHYcObAcyUmtP0I8Blg/Wms9uphHC0Ppl4132pZcSE7OnFDy671Xi5Yk9VZScLu572c3QN2mtb/gkSfrL8JYmktvGRVLCyN4s0CrEzcrrWtcUHsom/BR6owmQ+J+QebwGaAz+mMMs6Jlrrb8vz1rTV4abfSrXoNS0io7cG/ZgDFvZ8SZRIqIPRHNvavDNJSCoMr6UO9Cjmz56WBjItvvgl9Y29eqcDtgBchY5YLiOkDhEQzq/29+Vh8m66aSQ4mjMdxRz16jpdobDN"

# Redis
redis_ttl = 20*60  #20 minutes

# Lex
lex_api = "https://runtime.lex.us-east-1.amazonaws.com/bot/NewsBotOne/alias/NOneTester/user/user2030182/text"
lex_header = {
'X-Amz-Content-Sha256': 'beaead3198f7da1e70d03ab969765e0821b24fc913697e929e726aeaebf0eba3',
'X-Amz-Security-Token': 'FwoGZXIvYXdzEMb//////////wEaDBz27u+ZeQI89Eg5niLAAdnvC952lAcaY4to/RFqf2DQG4dQpNJv3NreNPMqURc8RHgc4GhjxgXVg/OTBH3mAFfqE4r3jgQma/tZNaL1bfkBKCR5NOHiUuifahUwbxkjuMF+V7R722P4LFokaPuMFeJOqeo6Omjnzu4jf6UdzURByJSuePs5DKB8jBTSjKXEK96goNr9xnslwDgXWsAvg1NgOHcJDnmklSLI0VTYTdAW1dJZ0Jg921SGfMGm1l9+neO543qVkfkCAmB4e75PzSitgJ2WBjIt6N8B3gD3Q8wsV3Vdxmx4PHum1ep0bfyuj9wpqtNtn9NFwgyrUwLzwwI5hHfB',
'X-Amz-Date': '20220707T233830Z',
'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIATBDRR2Z5LFLS5I7X/20220707/us-east-1/lex/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=b83f5a3030af86d648ccfdb6940c2780a0e88dcf7d4ed775cd9d5c0c32ebbc66',
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
get_doc = "http://52.90.191.191/get_relevant_docs"