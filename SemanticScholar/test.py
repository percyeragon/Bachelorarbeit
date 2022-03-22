import json
import requests
import argparse
import time
import os.path
if __name__ == '__main__':
    dois=[]
    parser = argparse.ArgumentParser()
    parser.add_argument("json_in_file")
    parser.add_argument("out_directory")
    args = parser.parse_args()
    if not os.path.exists(args.out_directory):
        os.mkdir(args.out_directory)
    with open(args.json_in_file,'r') as infile:
        data = json.load(infile)
        for obj in data:
            dois.append(obj["doi"])
    i=1
    responses=[]
    for item in dois:
        if os.path.exists("./"+args.out_directory+"/"+str(i)+".json"):
            print("DOI existiert schon")
        else:
            response = requests.get(url="https://api.semanticscholar.org/v1/paper/" + str(item))
            print("DOI:",item," Response:",response.status_code," Fortschritt:",i*100/len(dois))
            if response.status_code==200:
                data = response.json()
                with open("./"+args.out_directory+"/"+str(i)+".json", 'w') as outfile:
                    json.dump(data, outfile, indent=3)
            time.sleep(3)
        i=i+1



