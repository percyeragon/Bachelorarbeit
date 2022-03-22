PIPELINE='/home/percyeragon/total-recall/pipeline'
OUTPUT='/home/percyeragon/total-recall/pipeline/output'
QUERY='/home/percyeragon/total-recall/Datensaetze/genome_editing/query.txt'
RELEVANTVOLLTEXT='/home/percyeragon/AusgangslistenHiCal/Volltext/relevant_titel_abstract.csv'
AKPDK='/home/percyeragon'
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Titel/Ausgangsliste.json
cp -r $OUTPUT $AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Titel
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=/$RELEVANTVOLLTEXT AUSGANGSLISTE=$AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Abstract/Ausgangsliste.json
cp -r $OUTPUT $AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Abstract
cd $PIPELINE && make paramStart QUERY=$QUERY RELEVANT=$RELEVANTVOLLTEXT AUSGANGSLISTE=$AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Volltext/Ausgangsliste.json
cp -r $OUTPUT $AKPDK/AusgangslistenHiCal/AbstractTitelVolltext/Volltext