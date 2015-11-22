import json
import os
import re
import xlwt
from tempfile import TemporaryFile
from operator import itemgetter
from collections import Counter
os.chdir('/Users/dexikong/Desktop/Weibo')

mentionmk = []
mentionks = []
for file in os.listdir('statuses'):
    if file.startswith("2015"):
        i=0
        j=0
        for files in os.listdir('statuses/'+file):
            with open('statuses/'+file+'/'+files) as json_file:
                json_data = json.load(json_file)
                jd = json_data['user']
                gd = jd['gender']
                regex1 = re.compile('mk(.+?)',re.IGNORECASE)
                regex2 = re.compile('micheal(.+?)',re.IGNORECASE)
                regex3 = re.compile('ks(.+?)',re.IGNORECASE)
                regex4 = re.compile('kate(.+?)',re.IGNORECASE)
                searchobj1 = re.search(regex1,json.dumps(json_data))
                searchobj2 = re.search(regex2,json.dumps(json_data))
                searchobj3 = re.search(regex3,json.dumps(json_data))
                searchobj4 = re.search(regex4,json.dumps(json_data))                
                if searchobj1 or searchobj2:
                    i=i+1
                    mentionmk.append(gd)
                else:
                    i=i                    
                if searchobj3 or searchobj4:
                    j=j+1
                    mentionks.append(gd)
                else:
                    j=j
  
c1 = Counter(mentionmk)
c2 = Counter(mentionks)
print 'MKgenderbias:'
print c1.most_common(2)
print 'KSgenderbias:'
print c2.most_common(2)
