#!/bin/bash

# make-pages.sh - output the number of pages in a set of PDF documents

# Eric Lease Morgan <emorgan@nd.edu>
# July 10, 2015 - first cut; requires pdfinfo (http://www.foolabs.com/xpdf/)


# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

    echo "Usage: $0 <name>"
    exit 1
    
fi

# process each PDF file in the corpus
for FILE in $NAME/pdf/*.pdf; do

	# do the work and check
	PAGES=$( pdfinfo $FILE 2>/dev/null | grep Pages | cut -d ":" -f 2 | sed 's/ //g' )
	if [ ! $PAGES ]; then PAGES=1; fi
	
	# create an identifier
	ID=$( basename $FILE .pdf )
	
	# output
	printf "$ID\t$PAGES\n"

done

# done
exit 0
