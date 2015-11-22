import json
import os
import re
from operator import itemgetter
import datetime
os.chdir('/Users/dexikong/Desktop/Weibo')

mentionmk = []
mentionks = []
folder = raw_input("reposts or comments? ")
for file in os.listdir(folder):
    if file.startswith("2015"):
        i=0
        j=0
        for files in os.listdir(folder+'/'+file):
            with open(folder+'/'+file+'/'+files) as json_file:
                if files.endswith(".json"):
                    json_data = json.load(json_file)
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
                    else:
                        i=i                    
                    if searchobj3 or searchobj4:
                        j=j+1
                    else:
                        j=j
                
        mentionmk.append((file,i))
        mentionks.append((file,j))
print 'MKmention:', sorted(tuple(mentionmk),key=itemgetter(1),reverse=True)
print 'KSmention:', sorted(tuple(mentionks),key=itemgetter(1),reverse=True)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
date = []
from dateutil import parser

x_val = [x[0] for x in mentionmk]
y_val = [x[1] for x in mentionmk]
z_val = [x[1] for x in mentionks]
for dt in x_val:
    dt = parser.parse(dt)
    date.append(dt)


plt.plot_date(x=date, y=y_val, fmt="r-")
plt.title(folder+" count"+' MK(Red) / KS(Blue)')
plt.ylabel(folder)
plt.grid(True)


plt.plot_date(x=date, y=z_val, fmt="b-")
plt.show()




                   
