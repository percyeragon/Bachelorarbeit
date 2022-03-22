BERT='/mnt/ceph/storage/data-tmp/2021/akpdk/thesis-beiche/code/DeepCT/bert-base-uncased'
STANDARD='/mnt/ceph/storage/data-tmp/2021/akpdk/CEEDER_Ausgangslisten/ceeder2018'
DEEPCT='/mnt/ceph/storage/data-tmp/2021/akpdk/thesis-beiche/code/DeepCT'
OUTPUT='/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-trained-models/ceeder'

srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Referenzen/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/Referenzen/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/ReferenzenStemStop/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/ReferenzenStemStop/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Zitate/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/Zitate/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/ZitateStemStop/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/ZitateStemStop/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Titel/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/Titel/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$STANDARD,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/TitelStemStop/model.ckpt-8983 bert-base-uncased/bert_config.json $STANDARD/Normal/Ausgangsliste.json $STANDARD/TitelStemStop/Ausgangsliste.json