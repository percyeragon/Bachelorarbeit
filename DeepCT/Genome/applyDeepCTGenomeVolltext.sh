VOLLTEXT='/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/genome_editing/Volltext'
DEEPCT='/mnt/ceph/storage/data-tmp/2021/akpdk/thesis-beiche/code/DeepCT'
OUTPUT='/mnt/ceph/storage/data-tmp/2021/akpdk/DeepCT-Modelle'
BERT='/mnt/ceph/storage/data-tmp/2021/akpdk/thesis-beiche/code/DeepCT/bert-base-uncased'
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Referenzen/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/Referenzen/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/ReferenzenStemStop/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/ReferenzenStemStop/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Zitate/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/Zitate/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/ZitateStemStop/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/ZitateStemStop/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/Titel/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/Titel/Ausgangsliste.json
srun --gres gpu:ampere:1 -c 4 --mem=100G --container-writable --container-mounts=$VOLLTEXT,$BERT,$DEEPCT,$OUTPUT --container-workdir=$DEEPCT  --container-name=DeepCTMaik  --pty --chdir $DEEPCT python3 applyDeepCT.py $OUTPUT/TitelStemStop/model.ckpt-40258 bert-base-uncased/bert_config.json $VOLLTEXT/Normal/Ausgangsliste.json $VOLLTEXT/TitelStemStop/Ausgangsliste.json