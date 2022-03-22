from bs4 import BeautifulSoup
import os
from os.path import dirname, join
import json
import pandas as pd
import requests
import time
directory=("/mnt/ceph/storage/data-tmp/2021/akpdk/webisDatensatzProcessed") # location of XML files on local drive
result=[]
i=0
for infile in os.listdir(directory):
    filename=join(directory, infile)
    indata=open(filename,"r", encoding="utf-8", errors="ignore") # UTF-8 encoding errors are ignored
    contents = indata.read()
    soup = BeautifulSoup(contents,'xml')
    dois = soup.find_all(type="DOI") # get item document identifier (DOI)
    for doi in dois:
        DOI=doi.get_text()
        break
    result.append(str(DOI))

i=1
liste=[]
for item in result:
    response = requests.get(url="https://api.semanticscholar.org/v1/paper/" + str(item))
    print("DOI:",item," Response:",response.status_code," Fortschritt:",i*100/len(result))
    if response.status_code==200:
        data = response.json()
        liste.append(data)
    time.sleep(3)
    i=i+1
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/einfach/einfacherDatensatzJKI.json", 'w') as f:
    json.dump(liste, f)