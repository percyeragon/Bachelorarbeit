import json
import pandas as pd

df_fulltext = pd.DataFrame(columns=['titel', 'fulltext'])
df_normal = pd.DataFrame(columns=['nummer', 'titel'])
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/VolltextData.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        citations = " ".join(obj["citations"])
        references = " ".join(obj["references"])
        df_fulltext.loc[str(obj["nummer"])] = [str(obj["titel"]), str(obj["fulltext"])+" "+citations+" "+references]
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Normal/Ausgangsliste.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        df_normal.loc[str(obj["nummer"])] = [str(obj["nummer"]), str(obj["titel"])]
df_combined = df_fulltext.merge(df_normal, how='inner', on='titel')
titelabstractlist = []
with open("/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Standard/Normal/Ausgangsliste.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        for i in range(0, len(df_combined["nummer"])):
            if int(obj["nummer"]) == int(df_combined["nummer"][i]):
                break
        if int(obj["nummer"]) == int(df_combined["nummer"][i]):
            titelabstractdict = {
                "nummer": obj["nummer"],
                "titel": obj["titel"],
                "abstract": df_combined["fulltext"][i]
            }
        else:
            titelabstractdict = {
                "nummer": obj["nummer"],
                "titel": obj["titel"],
                "abstract": obj["abstract"]
            }
        titelabstractlist.append(titelabstractdict)
with open('/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/Volltext/Zitate+Referenzen/Ausgangsliste.json ','w') as outfile:
    json.dump(titelabstractlist,outfile,indent=3)