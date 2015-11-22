import json
import os
import re
import xlwt
from tempfile import TemporaryFile
#Change directory to Weibo
os.chdir('/Users/dexikong/Desktop/Weibo')
mentionmk = []
mentionks = []
mk=0
ks=0
mktotal = []
kstotal = []
i=0
j=0
for file in os.listdir('statuses'):
    if file.startswith("2015"):       
        for files in os.listdir('statuses/'+file):
            with open('statuses/'+file+'/'+files) as json_file:
                json_data = json.load(json_file)
                jd = json_data['user']
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
                mentionmk.append(jd['id'])
            else:
                i=i
            if searchobj3 or searchobj4:
                j=j+1
                mentionks.append(jd['id'])
            else:
                j=j

book = xlwt.Workbook()
sheet1 = book.add_sheet('sheet1')
for i,e in enumerate(mentionmk):
    sheet1.write(i+1,1,e)
sheet1.write(1,0,i)
sheet1.write(0,0,'MKTotal')
sheet1.write(0,1,'MKUser')
for i,e in enumerate(mentionks):
    sheet1.write(i+1,3,e)
sheet1.write(1,2,j)
sheet1.write(0,2,'KSTotal')
sheet1.write(0,3,'KSUser')
name = "wordcount1a.xls"
book.save(name)
book.save(TemporaryFile())
