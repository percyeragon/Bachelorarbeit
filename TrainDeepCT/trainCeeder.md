 
Die heruntergeladenen Dateien liegen im Ceph unter :

<code>/mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/ceeder-download-in-progress/semantic-scholar-papers</code>

Diese Dateien können wir mithilfe meines ParsingTools in eine Dokumentrepräsentation umwanden, aus denen wir die Relevanzlabel gewinnen können. Dabei benutzen unsere drei Strategien unterschiedliche Dokumentrepräsentation für das Training von DeepCT. Es gibt unterschidliche FLAGS, die  im ParsingTool verwendet werden können.
Diese FLAGS heißen wie die einzelnen Strategien: --referenzen / --zitate / --titel

<code> python3 parseCeeder.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/ceeder-download-in-progress/semantic-scholar-papers ./parsedCeeder.json --titel </code>

Mithilfe der erstellten Dokumentrepräsentation können wir die Relevanzlabel für das Training von DeepCT berechnen. FLAGS für das Tool sind <code>--stem</code> und <code>--stop</code>

<code>python3 passage_extraction_util.py ./parsedCeeder.json ./myalltrain.relevant.docterm_recall</code>

Durch den Erwerb der Relevanzlabel können wir nun DeepCT trainieren. Hier verweise ich auf die Anleitung, die im ReadMe steht.



In Progress Maik:

```
python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-referenzen-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-referenzen-docterm-recall-stem-stop.json --stem --stop

python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall-stem-stop.json --stem --stop

python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-zitate-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-zitate-docterm-recall-stem-stop.json --stem --stop
ceeder-zitate-strategey.json

python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-referenzen-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-referenzen-docterm-recall.json

python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-titel-docterm-recall.json

python3 passage_extraction_util.py /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-zitate-strategey.json /mnt/ceph/storage/data-in-progress/data-teaching/theses/wstud-thesis-beiche/deep-ct-training-data/ceeder/ceeder-zitate-docterm-recall.json
```

