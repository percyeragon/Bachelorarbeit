import json
import pandas as pd

df_fulltext = pd.DataFrame(columns=['titel', 'fulltext'])
df_normal = pd.DataFrame(columns=['nummer', 'titel'])
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/VolltextData.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        df_fulltext.loc[str(obj["nummer"])] = [str(obj["titel"]), str(obj["fulltext"])]
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Normal/Ausgangsliste.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        df_normal.loc[str(obj["nummer"])] = [str(obj["nummer"]), str(obj["titel"])]
df_combined = df_normal.merge(df_fulltext, how='inner', on='titel')
df_combined = df_combined.drop_duplicates(subset=['titel'])
print(df_combined)
titelabstractlist = []
i=0
for i in df_combined.index:
    titelabstractdict = {
        "nummer":  int(df_combined["nummer"][i]),
        "titel": df_combined["titel"][i],
        "abstract": df_combined["fulltext"][i]
     }
    titelabstractlist.append(titelabstractdict)
with open('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Normal/Ausgangsliste.json ','w') as outfile:
    json.dump(titelabstractlist,outfile,indent=3)