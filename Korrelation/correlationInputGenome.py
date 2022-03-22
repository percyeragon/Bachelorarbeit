import json
import pandas as pd
Titel = []
TitelStemStop = []
Referenzen = []
ReferenzenStemStop = []
Zitate = []
ZitateStemStop = []
mean = []

for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/Titel/myalltrain.relevant.docterm_recall"):
    Titel.append(json.loads(line))
for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/Referenzen/myalltrain.relevant.docterm_recall"):
    Referenzen.append(json.loads(line))
for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/Zitate/myalltrain.relevant.docterm_recall"):
    Zitate.append(json.loads(line))
for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/TitelStemStop/myalltrain.relevant.docterm_recall"):
    TitelStemStop.append(json.loads(line))
for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/ReferenzenStemStop/myalltrain.relevant.docterm_recall"):
    ReferenzenStemStop.append(json.loads(line))
for line in open("/mnt/ceph/storage/data-tmp/2021/akpdk/erweitert/ZitateStemStop/myalltrain.relevant.docterm_recall"):
    ZitateStemStop.append(json.loads(line))
i=0
for obj in Zitate:
    ZitateData = Zitate[i]
    ReferenzenData = Referenzen[i]
    TitelData = Titel[i]
    ZitateStemStopData = ZitateStemStop[i]
    ReferenzenStemStopData = ReferenzenStemStop[i]
    TitelStemStopData = TitelStemStop[i]
    ZitateTermRecall = []
    for key, value in ZitateData["term_recall"].items():
        ZitateTermRecall.append([key,value])
    ZitateDF = pd.DataFrame(ZitateTermRecall, columns=['word', 'Zitate'])
    ReferenzenTermRecall = []
    for key, value in ReferenzenData["term_recall"].items():
        ReferenzenTermRecall.append([key,value])
    ReferenzenDF = pd.DataFrame(ReferenzenTermRecall, columns=['word', 'Referenzen'])
    TitelTermRecall = []
    for key, value in TitelData["term_recall"].items():
        TitelTermRecall.append([key,value])
    TitelDF = pd.DataFrame(TitelTermRecall, columns=['word', 'Titel'])
    ZitateStemStopTermRecall = []
    for key, value in ZitateStemStopData["term_recall"].items():
        ZitateStemStopTermRecall.append([key, value])
    ZitateStemStopDF = pd.DataFrame(ZitateStemStopTermRecall, columns=['word', 'ZitateStemStop'])
    ReferenzenStemStopTermRecall = []
    for key, value in ReferenzenStemStopData["term_recall"].items():
        ReferenzenStemStopTermRecall.append([key, value])
    ReferenzenStemStopDF = pd.DataFrame(ReferenzenStemStopTermRecall, columns=['word', 'ReferenzenStemStop'])
    TitelStemStopTermRecall = []
    for key, value in TitelStemStopData["term_recall"].items():
        TitelStemStopTermRecall.append([key, value])
    TitelStemStopDF = pd.DataFrame(TitelStemStopTermRecall, columns=['word', 'TitelStemStop'])
    allTitlesDF = ZitateDF.merge(ReferenzenDF, how='outer', on='word')
    allTitlesDF = allTitlesDF.merge(TitelDF, how='outer', on='word')
    allTitlesDF = allTitlesDF.merge(TitelStemStopDF, how='outer', on='word')
    allTitlesDF = allTitlesDF.merge(ReferenzenStemStopDF, how='outer', on='word')
    allTitlesDF = allTitlesDF.merge(ZitateStemStopDF, how='outer', on='word')
    allTitlesDF = allTitlesDF.fillna(0)
    corrDF = allTitlesDF.corr(method ='spearman')
    mean.append(corrDF.stack())
    i=i+1
meanDF = pd.DataFrame(mean)
print(meanDF.mean())