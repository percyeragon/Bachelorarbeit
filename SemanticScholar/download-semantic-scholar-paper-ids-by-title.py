#!/usr/bin/env python3

import json
import requests
import time
from tqdm import tqdm
import os.path

def parsed_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument("--out_directory")
    return parser.parse_args()

def url_quote(string):
    from urllib.parse import quote
    return quote(string)

def file_name(args, string):
    import hashlib
    string = str(hashlib.md5(url_quote(string).encode('utf-8')).hexdigest()) + '.jsonl'

    return args.out_directory + '/' + string

if __name__ == '__main__':
    args = parsed_args()
    titles = [i for i in open(args.input_file,'r')]

    for title in tqdm(titles):
        out_dir = file_name(args, title)
        if os.path.exists(out_dir):
            continue

        request = "https://api.semanticscholar.org/graph/v1/paper/search?query=" + url_quote(title)
        response = requests.get(url=request)
        if response.status_code==200:
            data = response.json()
            with open(out_dir, 'w') as outfile:
                json.dump(data, outfile, indent=3)
        time.sleep(3)

