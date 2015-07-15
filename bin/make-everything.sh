#!/bin/bash

# make-everything.sh - one script to rule them all

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut; based on EEBO-TCP work
# July  9, 2015 - added make graphs


# get input
NAME=$1

# sanity check; needs additional error checking
if [ -z $NAME ]; then

    echo "Usage: cat <citations.xml> | $0 <name>"
    exit 1
    
fi

# stage #0 - initialize directory structure
echo "initializing directory structure"
./bin/initialize.sh $NAME

# state #1 - build corpus
echo "building corpus"
cat /dev/stdin | ./bin/make-corpus.pl $NAME
./bin/transform-pdf2text.sh $NAME

# stage #2 - create the index
echo "making index"
./bin/make-index.sh $NAME

# make dictionary
echo "making dictionary"
./bin/make-dictionary.py $NAME/index/ > $NAME/dictionary.db

# extract unique words
echo "extracting unique words"
cat $NAME/dictionary.db | ./bin/make-unique.py  > $NAME/unique.db

# stage #3 - create the catalog
echo "building catalog"
./bin/make-catalog.sh $NAME

# stage #4 - create sorted numeric reports
echo "creating numeric reports"
./bin/calculate-size.sh   $NAME                      | sort -k2 -n -r > $NAME/sizes.db
./bin/calculate-themes.sh $NAME etc/theme-colors.txt | sort -k2 -g -r > $NAME/calculated-colors.db
./bin/calculate-themes.sh $NAME etc/theme-names.txt  | sort -k2 -g -r > $NAME/calculated-names.db
./bin/calculate-themes.sh $NAME etc/theme-ideas.txt  | sort -k2 -g -r > $NAME/calculated-ideas.db

# create reports, sorted by coefficient: colors, names, ideas
echo "calculating themes"
./bin/calculate-themes.py -v $NAME/dictionary.db etc/theme-colors.txt > $NAME/dictionary-colors.db
./bin/calculate-themes.py -v $NAME/dictionary.db etc/theme-names.txt  > $NAME/dictionary-names.db
./bin/calculate-themes.py -v $NAME/dictionary.db etc/theme-ideas.txt  > $NAME/dictionary-ideas.db

# make graphs
echo "making graphs"
./bin/make-graphs.sh $NAME

# state 5 - analyze corpus and create pretty about page
echo "making about page"
./bin/make-about.sh $NAME > $NAME/about.db
./bin/transform-about2html.py $NAME > $NAME/about.html

# done
echo "Done"
exit 0
