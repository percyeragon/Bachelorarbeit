# Running the unit tests

```
nosetests
```
Should print something like:
```
....
----------------------------------------------------------------------
Ran 4 tests in 1.175s

OK
```


# Umwandlung der Anfragen und jeweiligen Dokumente zu Trainingsdaten:  

Zuerst werden die jeweiligen Dokumente und die relevanten Anfragen zu den Dokumenten benötigt Dabei gibt es zwei 
Methoden, mit einer Anfrage pro Dokument oder mit mehreren Anfragen pro Dokument. Beispiel:

Jede Zeile: {"queries": ["what kind of animals are in grasslands", "tropical grasslands animals", ...], "doc":{"title": Tropical grassland animals (which do not all occur in the same area) include giraffes, zebras, buffaloes, ka...}}  

Diese Dictionaries werden dann zeilenweise abgespeichert und an ein Skript übergeben, dass die "term-recall" Werte von dem Referenzfeld mit den Anfragen extrahiert.  

Das Skript für die Ermittlung der Relevanzlabel per Dokument heißt passage_extraction_util.py und wird dann wie folgt aufgerufen:  
<code>python3 passage_extraction_util.py passage eingabedatei.json myalltrain.relevant.docterm_recall (optional --stem --stop)  </code>




# Prepare DeepCT Image in Slurm

First, create your enroot image:
```
srun -c 4  --mem=100G --container-image=nvcr.io#nvidia/tensorflow:20.06-tf1-py3 --container-name=DeepCT --pty echo "Image created sucessfully"
```

Clone DeepCT:
```
srun -c 4  --mem=100G --container-name=DeepCT --container-writable --pty git clone https://github.com/AdeDZY/DeepCT.git
```

Download BERT:
```
srun -c 4  --mem=100G --container-name=DeepCT --container-writable --pty bash -c 'wget https://storage.googleapis.com/bert_models/2020_02_20/uncased_L-12_H-768_A-12.zip && mkdir bert-uncased_L-12_H-768_A-12 && unzip uncased_L-12_H-768_A-12.zip -d bert-uncased_L-12_H-768_A-12 && rm -f uncased_L-12_H-768_A-12.zip' 
```

# Train DeepCT with Slurm

After you have executed the steps to [prepare your DeepCT image in slurm](#prepare-deepct-image-in-slurm), you can train the model with the following commands.

Assume you have the following files/directories:
- `<PATH-TO-TRAIN-DOCTERM-RECALL>`: the training data file produced as [described above](umwandlung-der-anfragen-und-jeweiligen-dokumente-zu-trainingsdaten).
- `<OUTPUT-DIRECTORY>`: directory where the trained model will be stored.

You can train your model with the following command:

```
srun \
    --gres gpu:ampere:1 -c 4  --mem=100G \
    --container-mounts=<PATH-TO-TRAIN-DOCTERM-RECALL>,<OUTPUT-DIRECTORY> \
    --chdir /workspace/DeepCT \
    --container-name=DeepCT --pty \
    python3 run_deepct.py \
        --task_name=marcodoc \
        --do_train=true \
        --do_eval=false \
        --do_predict=false \
        --data_dir=<PATH-TO-TRAIN-DOCTERM-RECALL> \
        --vocab_file=/workspace/bert-uncased_L-12_H-768_A-12/vocab.txt \
        --bert_config_file=/workspace/bert-uncased_L-12_H-768_A-12/bert_config.json \
        --init_checkpoint=/workspace/bert-uncased_L-12_H-768_A-12/bert_model.ckpt \
        --max_seq_length=128 \
        --train_batch_size=16 \
        --learning_rate=2e-5 \
        --num_train_epochs=3.0 \
        --recall_field=title \
        --output_dir=<OUTPUT-DIRECTORY>
```

Maik Training in Progress:

TitelStemStop
```
srun \
    --gres gpu:ampere:1 -c 4  --mem=100G \
    --container-mounts=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall-stem-stop.json,/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-trained-models/ceeder/TitelStemStop \
    --chdir /workspace/DeepCT \
    --container-name=DeepCT --pty \
    python3 run_deepct.py \
        --task_name=marcodoc \
        --do_train=true \
        --do_eval=false \
        --do_predict=false \
        --data_dir=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall-stem-stop.json \
        --vocab_file=/workspace/bert-uncased_L-12_H-768_A-12/vocab.txt \
        --bert_config_file=/workspace/bert-uncased_L-12_H-768_A-12/bert_config.json \
        --init_checkpoint=/workspace/bert-uncased_L-12_H-768_A-12/bert_model.ckpt \
        --max_seq_length=128 \
        --train_batch_size=16 \
        --learning_rate=2e-5 \
        --num_train_epochs=3.0 \
        --recall_field=title \
        --output_dir=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-trained-models/ceeder/TitelStemStop
```

Titel
```
srun \
    --gres gpu:ampere:1 -c 4  --mem=100G \
    --container-mounts=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall.json,/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-trained-models/ceeder/Titel \
    --chdir /workspace/DeepCT \
    --container-name=DeepCT --pty \
    python3 run_deepct.py \
        --task_name=marcodoc \
        --do_train=true \
        --do_eval=false \
        --do_predict=false \
        --data_dir=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall.json \
        --vocab_file=/workspace/bert-uncased_L-12_H-768_A-12/vocab.txt \
        --bert_config_file=/workspace/bert-uncased_L-12_H-768_A-12/bert_config.json \
        --init_checkpoint=/workspace/bert-uncased_L-12_H-768_A-12/bert_model.ckpt \
        --max_seq_length=128 \
        --train_batch_size=16 \
        --learning_rate=2e-5 \
        --num_train_epochs=3.0 \
        --recall_field=title \
        --output_dir=/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-trained-models/ceeder/Titel
```

Remaining: Zitate, ZitateStemStop, Referenzen, ReferenzenStemStop
