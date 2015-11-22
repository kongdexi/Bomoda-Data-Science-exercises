import json
import os
import re
from collections import Counter
user = []
location = []
os.chdir('/Users/dexikong/Desktop/Weibo')
for file in os.listdir('statuses'):
    if file.startswith("2015"):       
        for files in os.listdir('statuses/'+file):
            with open('statuses/'+file+'/'+files) as json_file:
                json_data = json.load(json_file)
                jd = json_data['user']
                user.append(jd['id'])
                location.append(jd['location'].encode('ascii','ignore'))

c = Counter(user)
print c.most_common(10)

