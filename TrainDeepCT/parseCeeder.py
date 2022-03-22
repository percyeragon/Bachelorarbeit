import json
import os
import argparse
from glob import glob
from tqdm import tqdm

def titel(json_files,outFile):
    for file in json_files:
        print(file)
        for line in tqdm(open(file)):
            data = json.loads(line)
            titel = data["title"]
            abstract = str(data["match-semantic-scolar"]["abstract"])
            document = {
                "queries" : [titel],
                "doc" : {
                    "title" : abstract
                }
            }
            with open(outFile,'a') as outfile:
                json.dump(document, outfile)
                outfile.write("\n")

def zitate(json_files,outFile):
    for file in json_files:
        for line in tqdm(open(file)):
            data = json.loads(line)
            citations = []
            for obj in data["match-semantic-scolar"]["citations"]:
                citations.append(obj["title"])
            abstract = str(data["match-semantic-scolar"]["abstract"])
            document = {
                "queries" : citations,
                    "doc" : {
                    "title" : abstract
                }
            }
            with open(outFile,'a') as outfile:
                json.dump(document, outfile)
                outfile.write("\n")

def referenzen(json_files,outFile):
    for file in json_files:
        for line in tqdm(open(file)):
            data = json.loads(line)
            references = []
            for obj in data["match-semantic-scolar"]["citations"]:
                references.append(obj["title"])
            abstract = str(data["match-semantic-scolar"]["abstract"])
            document = {
                "queries" : references,
                "doc" : {
                    "title" : abstract
                }
            }
            with open(outFile,'a') as outfile:
                json.dump(document, outfile)
                outfile.write("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_infile", help="")
    parser.add_argument("out_file", help="trainingfile with relevancelabels for DeepCT")
    parser.add_argument("--titel", action="store_true", help="pick your strategy like your starter pokemon")
    parser.add_argument("--zitate", action="store_true")
    parser.add_argument("--referenzen", action="store_true")
    args = parser.parse_args()
    json_files = glob(args.path_infile + "**/*", recursive=True)
    if args.titel:
        titel(json_files,args.out_file)
    if args.zitate:
        zitate(json_files,args.out_file)
    if args.referenzen:
        referenzen(json_files,args.out_file)