#!/usr/bin/env python3

import json
import requests
import time
from tqdm import tqdm
import os.path

def tokenize(title):
    from nltk.stem import PorterStemmer
    stemmer = PorterStemmer()
    title = title.strip().lower().split()

    return [stemmer.stem(i) for i in title]

def jaccard(a,b):
    a = set(tokenize(a))
    b = set(tokenize(b))
    c = a.intersection(b)

    return float(len(c)) / (len(a) + len(b) - len(c))

# real unit tests in the next iteration :)
assert ['the', 'impact', 'of', 'dietari', 'transit', 'metal', 'on', 'host-bacteri', 'interact'] == tokenize('The Impact of Dietary Transition Metals on Host-Bacterial Interactions')
assert 1.0 <= jaccard('The Impact of Dietary Transition Metals on Host-Bacterial Interactions', 'The Impact of Dietary Transition Metals on Host-Bacterial Interactions')
assert 0.7 <= jaccard('The impact of dietary Metals on Bacterial Interactions', 'The Impact of Dietary Transition Metals on Host-Bacterial Interactions')

def parsed_args():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument("--response_directory")
    parser.add_argument("--output_file")
    return parser.parse_args()

def url_quote(string):
    from urllib.parse import quote
    return quote(string)

def file_name(args, string):
    import hashlib
    string = str(hashlib.md5(url_quote(string).encode('utf-8')).hexdigest()) + '.jsonl'

    return args.response_directory + '/' + string

if __name__ == '__main__':
    args = parsed_args()
    titles = [i for i in open(args.input_file,'r')]
    covered_titles = set([json.loads(i)['title'] for i in open(args.output_file,'r')])

    with open(args.output_file, 'a') as out:
        for title in tqdm(titles):
            json_file = file_name(args, title)
            if not(os.path.exists(json_file)) or title in covered_titles:
                continue

            data = json.load(open(json_file))['data']
            data = [(i, jaccard(i['title'], title)) for i in data]
            data = [i for i in data if i[1] >= 0.75]
            if len(data) != 1:
                continue

            response = requests.get(url='https://api.semanticscholar.org/v1/paper/' + data[0][0]['paperId'])
            if response.status_code==200:
                out.write(json.dumps({
                    'title': title,
                    'match-semantic-scolar': response.json(),
                    'title-jaccard-similarity': data[0][1]
                }) + '\n')
                out.flush()
        
            time.sleep(3)

