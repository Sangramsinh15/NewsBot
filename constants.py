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
  'X-Amz-Security-Token': 'FwoGZXIvYXdzEDkaDOloHkT7ji5MHpSvMiLAAaCNLhnVRlLaioplwJ2KHPWvgMqfV/ADpn+m2kT3gLEtT6g/Lj2zp0PlH8ZvJUk3U8VGe8ACVNDbYLEbKeqf6PVdnhnezM8ZY7TJKgfGshqmUq4AGi1QPOrq0+2d0KIKrkg3tcLQNwNKJxl37k0h5983rBhXVlyXF8LV+tWZAh1c336LZfAgMI4e3SHOvA1allIzA35xeQO/7yDgy6CxSeIHRI4buABVdq9gUXx4jgAwvGAsVVqeLGPcJtwAKMB2HyijtbaWBjItwJFJvOcRwYj9AqAdea6hGEMquSEZpY9T2M9IYl79ERMExCxDdRbBm8SYX6AZ',
  'X-Amz-Date': '20220712T160421Z',
  'Authorization': 'AWS4-HMAC-SHA256 Credential=ASIAX5UJGMCWYGCIRX5R/20220712/us-east-1/lex/aws4_request, SignedHeaders=host;x-amz-content-sha256;x-amz-date;x-amz-security-token, Signature=c93fbe697a55f8d7eaf279aa023405b7432aeaf8550ef54df0e2a00b745cf8c0',
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