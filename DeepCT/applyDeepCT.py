import pyterrier as pt
pt.init()
import os
import textwrap
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import pyterrier_deepct
import pandas as pd
import json
import argparse
from tqdm import tqdm

def applyDeepCT(modelfile,bertfile,infile):
    deepct = pyterrier_deepct.DeepCTTransformer(bertfile,
                                                modelfile,
                                                max_seq_length=512)
    titelabstractlist = []
    df_abstract = pd.DataFrame(columns=['text', 'docno'])
    df_title = pd.DataFrame(columns=['text', 'docno'])
    abstracts = []
    titels = []
    docno = []
    with open(infile, 'r') as f:
        data = json.load(f)
        for obj in data:
            abstract = str(obj["abstract"])
            titel = str(obj["titel"])
            if len(str(obj["abstract"]).split()) > 512:
                teilungen = textwrap.wrap(abstract, width=512)
                docno.append(obj["nummer"])
                for teilung in teilungen:
                    abstracts.append([str(teilung), str(obj["nummer"])])
                    titels.append([str(titel), str(obj["nummer"])])
            else:
                df_abstract.loc[str(obj["nummer"])] = [str(obj["abstract"]), str(obj["nummer"])]
                df_title.loc[str(obj["nummer"])] = [str(obj["titel"]), str(obj["nummer"])]
    df_abstract_teilung = pd.DataFrame(data=abstracts, columns=['text', 'docno'])
    df_titel_teilung = pd.DataFrame(data=titels, columns=['text', 'docno'])
    deepct_df_abstract_teilung = deepct(df_abstract_teilung)
    deepct_df_titel_teilung = deepct(df_titel_teilung)
    for obj in docno:
        df_mask_abstract = deepct_df_abstract_teilung["docno"] == str(obj)
        df_mask_titel = deepct_df_titel_teilung["docno"] == str(obj)
        filtered_df_abstract = deepct_df_abstract_teilung[df_mask_abstract]
        filtered_df_titel = deepct_df_titel_teilung[df_mask_titel]
        titel = str(filtered_df_titel['text'].iloc[0])
        abstract = " ".join(filtered_df_abstract["text"])
        titelabstractlist.append({"nummer": obj, "titel": str(titel), "abstract": str(abstract)})

    deepct_df_abstract = deepct(df_abstract)
    deepct_df_title = deepct(df_title)

    for i in deepct_df_abstract.index:
        titel = deepct_df_title["text"][i]
        abstract = deepct_df_abstract["text"][i]
        titelabstractlist.append(
            {"nummer": int(deepct_df_abstract["docno"][i]), "titel": str(titel), "abstract": str(abstract)})
    return titelabstractlist


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("model_file", help="modelfile = trained Model with DeepCT : model.ckpt-40258")
    parser.add_argument("bert_file", help="bert_config.json")
    parser.add_argument("in_file", help="all pre-weighted documents in dictionaries without DeepCT")
    parser.add_argument("out_file", help="all weighted documents in dictionaries with DeepCT")
    args = parser.parse_args()
    with open(args.out_file, 'w') as f:
      json.dump(applyDeepCT(args.model_file,args.bert_file,args.in_file), f, indent=3)



