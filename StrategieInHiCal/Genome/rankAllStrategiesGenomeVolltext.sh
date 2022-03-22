RELEVANTVOLLTEXT='/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/genome_editing/Volltext/relevant_titel_abstract.csv'
PIPELINE='/home/percyeragon/total-recall/pipeline'
OUTPUT='/home/percyeragon/total-recall/pipeline/output'
RESULTS='/home/percyeragon/total-recall/pipeline/data/results'
QUERY='/mnt/ceph/storage/data-tmp/2021/akpdk/total-recall/Datensaetze/genome_editing/query.txt'
AUSGANGSLISTEN='/home/percyeragon/AusgangslistenHiCal/genome_editing'
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/Normal/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/Normal
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/Normal
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/Referenzen/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/Referenzen
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/Referenzen
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=/$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/ReferenzenStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/ReferenzenStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/ReferenzenStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/Titel/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/Titel
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/Titel
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/TitelStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/TitelStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/TitelStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/Zitate/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/Zitate
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/Zitate
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AUSGANGSLISTEN/Volltext/ZitateStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Volltext/ZitateStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Volltext/ZitateStemStop
rm -rf $PIPELINE/data