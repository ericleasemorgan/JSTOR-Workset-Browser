#!/bin/bash

# transform-pdf2text.sh - use TIKA to extract text from PDF files

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - based on previous work (https://gist.github.com/ericleasemorgan/c4e34ffad96c0221f1ff)
# July  9, 2015 - checked for existence of file before processing; faster and more efficient


# configure
HOST='127.0.0.1'
TIKA='./etc/tika.jar'
MODE="--text"
PORT=12345
PDF='pdf'
TEXT='text'

# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

	echo "Usage: $0 <name>"
	exit 1
	
fi

# start TIKA
printf "Starting TIKA"
java -jar $TIKA $MODE --server -port $PORT &
PID=$!
echo " ($PID)..."
sleep 10

# process each PDF file in the collection's cache
for FILE in $NAME/$PDF/*.pdf
do

    # create an output filename
    TEXTFILE=$( basename $FILE .pdf )
    TEXTFILE="$NAME/$TEXT/$TEXTFILE.txt"
	
	# do the work
	echo $FILE
	if [ ! -e $TEXTFILE ]; then nc $HOST $PORT < $FILE > $TEXTFILE; fi
	
done

# stop TIKA
echo "Stopping TIKA ($PID)..."
kill $PID

# done
exit 0
