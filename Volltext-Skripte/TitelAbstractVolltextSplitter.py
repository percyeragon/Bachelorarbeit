import json
import pandas as pd

df_fulltext = pd.DataFrame(columns=['titel', 'fulltext'])
df_normal = pd.DataFrame(columns=['nummer', 'titel', 'abstract'])
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/VolltextData.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        df_fulltext.loc[str(obj["nummer"])] = [str(obj["titel"]), str(obj["fulltext"])]
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Normal/Ausgangsliste.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        df_normal.loc[str(obj["nummer"])] = [str(obj["nummer"]), str(obj["titel"]),str(obj["abstract"])]
df_combined = df_normal.merge(df_fulltext, how='inner', on='titel')
df_combined = df_combined.drop_duplicates(subset=['titel'])
titelList = []
abstractList = []
volltextList = []
i=0
for i in df_combined.index:
    titelDict = {
        "nummer": int(df_combined["nummer"][i]),
        "titel": df_combined["titel"][i],
        "abstract": ""
    }
    abstractDict = {
        "nummer":  int(df_combined["nummer"][i]),
        "titel": "",
        "abstract": df_combined["abstract"][i]
     }
    volltextDict = {
        "nummer":  int(df_combined["nummer"][i]),
        "titel": "",
        "abstract": df_combined["fulltext"][i]
     }
    titelList.append(titelDict)
    abstractList.append(abstractDict)
    volltextList.append(volltextDict)
with open('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/AbstractTitelVolltext/Abstract/Ausgangsliste.json','w') as outfile:
    json.dump(abstractList,outfile,indent=3)
with open('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/AbstractTitelVolltext/Titel/Ausgangsliste.json','w') as outfile:
    json.dump(titelList,outfile,indent=3)
with open('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/AbstractTitelVolltext/Volltext/Ausgangsliste.json','w') as outfile:
    json.dump(volltextList,outfile,indent=3)