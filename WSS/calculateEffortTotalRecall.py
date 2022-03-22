import json
import os
import pandas as pd
from tqdm import tqdm
from glob import glob
dataset_path = "/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/"
rankings = {}
recall_files = glob(dataset_path+"**/*bmi_42.avg.precisionrecall", recursive=True)


for file in recall_files:
    docFile = os.path.split(os.path.split(file)[0])[0]
    with open(file, 'r') as infile:
        df = pd.read_csv(file, sep=" ")
        df = df.dropna(how='all', axis='columns')
        df.columns = ['type', 'relevantDocuments','cutoff','recall','effort','precision','f1-score']
        effort100= df["effort"][len(df)-1]
        path_split = file.split(os.path.sep)
        Strategie = path_split[len(path_split) - 3]
        Repräsentation = path_split[len(path_split) - 4]
        Datensatz = path_split[len(path_split) - 5]
        print(Strategie,Repräsentation,Datensatz,effort100)