import json
import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("json_in_file", help="Each line: {\"queries\": [\"what kind of animals are in grasslands\", \"tropical grasslands animals\", ...], \"doc\":{\"title\": Tropical grassland animals (which do not all occur in the same area) include giraffes, zebras, buffaloes, ka...}}")
    parser.add_argument("json_out_file", help="all documents in dcitionaries")
    args = parser.parse_args()
    data = []
    for line in open(args.json_in_file):
        data.append(json.loads(line))
    titelabstractlist= []
    i=0
    for obj in data:
        abstract = obj["doc"]["title"]
        titelabstractlist.append({"nummer": i, "titel": "" , "abstract": str(abstract)})
        i=i+1
    with open(args.json_out_file, 'w') as outfile:
        json.dump(titelabstractlist, outfile, indent=3)
