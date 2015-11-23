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
                lc = jd['location']
                text = json.dumps(lc)
                location.append(text)                

c = Counter(user)
locations = Counter(location)
print c.most_common(10)
chinese = locations.most_common(10)
for location in chinese:
    print location[0].decode('unicode_escape') + '%d' % (location[1])

