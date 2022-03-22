from bs4 import BeautifulSoup
import os
from os.path import dirname, join
import json
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
    titles=soup.find_all('title') # get item title
    for title in titles:
        TITLE=title.get_text()
        break
    abstracts=soup.find_all('abstract')
    for abstract in abstracts:
        ABSTRACT=abstract.get_text()
    fulltexts = soup.find_all('body')
    for fulltext in fulltexts:
        FULLTEXT = fulltext.get_text()
    response = requests.get(url="https://api.semanticscholar.org/v1/paper/" + str(DOI))
    if response.status_code==200:
        data = response.json()
    citations = []
    for obj in data["citations"]:
        citations.append(obj["title"])
    references = []
    for obj in data["references"]:
        references.append(obj["title"])
    time.sleep(3)
    mydict = {
        "nummer": str(i),
        "titel": str(TITLE),
        "abstract": str(ABSTRACT),
        "doi" : str(DOI),
        "fulltext" : str(FULLTEXT),
        "citations" : citations,
        "references": references
    }
    result.append(mydict)
    i=i+1
with open('/home/percyeragon/FulltextAusgangsliste.json', 'w') as outfile:
    json.dump(result, outfile, indent=3)