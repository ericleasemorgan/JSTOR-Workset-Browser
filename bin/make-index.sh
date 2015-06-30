#!/bin/bash

# make-index.sh - create frequency files from the contents of a directory

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first investigations; based on EEBO-TCP work

# configure
TXT2FREQUENCY=./bin/make-index.py

# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# process each json file in the given directory
echo "indexing and building text files"
for FILE in $NAME/text/*.txt
do
    
    # parse out the KEY and echo
    KEY=$( basename $FILE .txt )
		
	# index
	if [ ! -f "$NAME/index/$KEY.db" ]; then
	
		echo "building $NAME/index/$KEY.db"
		cat $FILE | $TXT2FREQUENCY > $NAME/index/$KEY.db
	
	fi
		
done
