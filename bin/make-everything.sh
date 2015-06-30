#!/bin/bash

# make-everything.sh - one script to rule them all

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut; based on EEBO-TCP work

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
cat /dev/stdin | ./bin/harvest.pl $NAME
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

# done
echo "Done"
exit 0
