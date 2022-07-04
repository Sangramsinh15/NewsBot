#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 15:48:21 2022

@author: sangrammore
"""
import feedparser
import re
import json
import time
import random
import hashlib
import datetime
from dateutil.parser import parse
import TOI_Links
import constants
from s3Utilities import S3Utilities

class toiCrawler:
    def __init__(self):
        self.s3_obj = S3Utilities(constants.aws_access_key_id, constants.aws_secret_access_key, constants.aws_session_token)
                
    def hash_url(self,url):
        return (hashlib.md5(url.encode())).hexdigest()

    def date_clean(self,date):
        readable_time, unix_timestamp = None, None
        if not readable_time or not unix_timestamp:
            try:
                dt=parse(date)
                readable_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                unix_timestamp = int(dt.timestamp())
            except:
                pass
        if not readable_time or not unix_timestamp:
            try:
                dt=datetime.datetime.fromisoformat(date)
                readable_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                unix_timestamp = int(dt.timestamp())
            except:
                pass
        if not readable_time or not unix_timestamp:
            try:
                dt=datetime.datetime.strptime(date, "%a, %d %b %Y %H:%M:%S PT")
                readable_time = dt.strftime("%Y-%m-%d %H:%M:%S")
                unix_timestamp = int(dt.timestamp())
            except:
                pass
        return readable_time, unix_timestamp
    
                    
    def main(self):
        
        TAG_RE = re.compile(r'<[^>]+>')
        
        myJSON={}
        myList=[]  
        for index,i in enumerate(TOI_Links.links):
            NewsFeed = feedparser.parse(i["Link"])
            time.sleep(random.choice([1,2,3]))
            
            print ('Number of RSS posts :', len(NewsFeed.entries))            
                
            for post in NewsFeed.entries:
                readable_time, unix_timestamp = self.date_clean(post.published)
                u=self.hash_url(post.link)
                desc=TAG_RE.sub('', post.description)
                if(desc.strip()==""):
                    new_desc = post.title
                else:
                    new_desc = desc.strip()
                tempList={'title': post.title,'link':post.link,'readable_time':readable_time,'unix_timestamp':unix_timestamp,'description':desc.strip(),'new_description':new_desc,'source_tag':i["Tag"],'hash_url':u}
                myList.append(tempList.copy())
        
        myJSON=json.dumps(myList, indent=4)
        file_key = "toi/{0}.json".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        self.s3_obj.write_data(data=myJSON, bucket=constants.bucket_name, file_key=file_key)

def lambda_handler(event, context):
    # TODO implement
    cls_obj = toiCrawler()
    cls_obj.main()

if __name__ == "__main__":
    lambda_handler(None, None)
    # cls_obj = toiCrawler()
    # cls_obj.main()
                                    
                
#     print(myJSON)
    
#     with open('dataDump1.json', 'w') as f:
#         json.dump(myList, f)

  

    