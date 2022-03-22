import json
import os
import pandas as pd
from tqdm import tqdm
from glob import glob
dataset_path = "/mnt/ceph/storage/data-tmp/2021/akpdk/CEEDER_Ausgangslisten/"
rankings = {}
recall_files = glob(dataset_path+"**/*bmi_42.avg.precisionrecall", recursive=True)

def calculateWSS(effort,totalDocuments,recall):
    wss = ((totalDocuments-effort)/(totalDocuments))-(1-recall)
    return wss


for file in recall_files:
    docFile = os.path.split(os.path.split(file)[0])[0]
    with open(docFile + "/Ausgangsliste.json", 'r') as niceFile:
        data = json.load(niceFile)
    with open(file, 'r') as infile:
        df = pd.read_csv(file, sep=" ")
        df = df.dropna(how='all', axis='columns')
        df.columns = ['type', 'relevantDocuments','cutoff','recall','effort','precision','f1-score']
        effort85= df["effort"][len(df)-4]
        effort90 = df["effort"][len(df) - 3]
        effort95 = df["effort"][len(df) - 2]
        totalDocs = len(data)
        wss85 = calculateWSS(effort85,totalDocs,0.85)
        wss90 = calculateWSS(effort85, totalDocs, 0.90)
        wss95 = calculateWSS(effort85, totalDocs, 0.95)
        path_split = file.split(os.path.sep)
        Strategie = path_split[len(path_split) - 3]
        Repräsentation = path_split[len(path_split) - 4]
        Datensatz = path_split[len(path_split) - 5]
        print(Strategie,Repräsentation,Datensatz,round(wss85,4),round(wss90,4),round(wss95,4))