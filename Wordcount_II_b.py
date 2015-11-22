import json
import os
import re
from datetime import datetime
from dateutil.parser import parse
os.chdir('/Users/dexikong/Desktop/Weibo')
i=0
j=0
post = []
for file in os.listdir('statuses'):
    if file.startswith("2015"):
        for files in os.listdir('statuses/'+file):
            with open('statuses/'+file+'/'+files) as json_file:
                json_data = json.load(json_file)
                jd = json_data['user']
                time = jd['created_at']
                t1 = parse(str(time))
                post.append(t1.hour)
                              
def peakhour(lst):
    return max(set(lst), key=lst.count)
print peakhour(post)
