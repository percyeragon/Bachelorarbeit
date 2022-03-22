PIPELINE='/home/percyeragon/total-recall/pipeline'
OUTPUT='/home/percyeragon/total-recall/pipeline/output'
QUERY='/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/ceeder2018/Standard/query.txt'
RELEVANT='/mnt/ceph/storage/data-tmp/2021/akpdk/AusgangslistenHiCal/ceeder2018/Standard/relevant_titel_abstract.csv'
AUSGANGSLISTEN='/home/percyeragon/CEEDER_Ausgangslisten/ceeder2018'
RESULTS='/home/percyeragon/total-recall/pipeline/data/results'

cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/Normal/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Normal
cp -r $RESULTS $AUSGANGSLISTEN/Normal
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/Referenzen/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Referenzen
cp -r $RESULTS $AUSGANGSLISTEN/Referenzen
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=/$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/ReferenzenStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/ReferenzenStemStop
cp -r $RESULTS $AUSGANGSLISTEN/ReferenzenStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/Titel/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Titel
cp -r $RESULTS $AUSGANGSLISTEN/Titel
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/TitelStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/TitelStemStop
cp -r $RESULTS $AUSGANGSLISTEN/TitelStemStop
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/Zitate/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/Zitate
cp -r $RESULTS $AUSGANGSLISTEN/Zitate
rm -rf $PIPELINE/data
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANT AUSGANGSLISTE=$AUSGANGSLISTEN/ZitateStemStop/Ausgangsliste.json
cp -r $OUTPUT $AUSGANGSLISTEN/ZitateStemStop
cp -r $RESULTS $AUSGANGSLISTEN/ZitateStemStop
rm -rf $PIPELINE/data