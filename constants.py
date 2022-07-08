# General AWS Credentials
aws_access_key_id="ASIAX5UJGMCW2BW4MI5D"
aws_secret_access_key="NDueB46lNnLMc2/EJKzKmi8z4ClSWEUclD+gB8fa"
aws_session_token="FwoGZXIvYXdzEMf//////////wEaDH+WaxkE216yEdVXOyLAAXdOc2cBgqqwgyA0QjxVZq4DzxmQ+zpbLIR6nO7dKw+TtGRiwi+4XHqTN63Hw3F7j08zEvsGXuHtAj2yPZ54WbxBricpDOC+3A5sfisNdqo/V/W2raLrbAgxj48x9ZOvUQcZs02vkA0WPhCCjd3HzYvKYfvDpJHNqavFTjePsUGE9Pvt3cCm3W3EZZTz3uTjiJWp2weEuAB3uL0a2NCUW7JMcuBDEyQmV+Yuk041TRnLSa638AP3zzA9zaK4sdPDciiimZ2WBjItceuTPpQOogfclIVJHfdpyx+kDP3J75TNybDd4gtzw1wzQ63dpPJDr40RqyrS"

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

# Dynamo-DB Details
table_name = "news_data"

# APIs
get_doc = "http://18.233.156.42/get_relevant_docs"