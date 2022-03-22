import pandas as pd
import json

df = pd.read_csv('/home/percyeragon/total-recall/Datensaetze/genome_editing/relevant_titel_abstract.csv')
relevantTitel = df['1'].tolist()
volltext = []
with open("/home/percyeragon/AusgangslistenHiCal/Volltext/Ausgangsliste.json", 'r') as infile:
    data = json.load(infile)
    for obj in data:
        volltext.append(obj["nummer"])
relevanteVolltext = list(set(relevantTitel) & set(volltext))
relevanteVolltext.sort()
df1 = pd.DataFrame(relevanteVolltext)
df1.to_csv('/home/percyeragon/AusgangslistenHiCal/Volltext/relevant_titel_abstract.csv', header=None, index=False)
