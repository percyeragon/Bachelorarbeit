PIPELINE='/home/percyeragon/total-recall/pipeline'
OUTPUT='/home/percyeragon/total-recall/pipeline/output'
RESULTS='/home/percyeragon/total-recall/pipeline/data/results'
QUERY='/mnt/ceph/storage/data-tmp/2021/akpdk/total-recall/Datensaetze/genome_editing/query.txt'
RELEVANTSTANDARD='/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/genome_editing/Standard/relevant_titel_abstract.csv'
AUSGANGSLISTEN='/home/percyeragon/AusgangslistenHiCal/genome_editing'

cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/Normal/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/Normal
cp -r $RESULTS $AUSGANGSLISTEN/Standard/Normal
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/Referenzen/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/Referenzen
cp -r $RESULTS $AUSGANGSLISTEN/Standard/Referenzen
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=/$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/ReferenzenStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/ReferenzenStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Standard/ReferenzenStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/Titel/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/Titel
cp -r $RESULTS $AUSGANGSLISTEN/Standard/Titel
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/TitelStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/TitelStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Standard/TitelStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/Zitate/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/Zitate
cp -r $RESULTS $AUSGANGSLISTEN/Standard/Zitate
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTSTANDARD AUSGANGSLISTE=$AUSGANGSLISTEN/Standard/ZitateStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Standard/ZitateStemStop
cp -r $RESULTS $AUSGANGSLISTEN/Standard/ZitateStemStop
rm -rf $PIPELINE/data