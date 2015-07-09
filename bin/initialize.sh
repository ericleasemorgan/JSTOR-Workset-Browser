#!/bin/bash

# initialize.sh - create a directory structure to hold our data

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut
# July  9, 2015 - made pdf and text directories readable only by me; can you say "copyright"?


# get input
NAME=$1

# sanity check
if [ -z $NAME ]; then

	echo "Usage: $0 <name>"
	exit 1
	
fi

# do the work
mkdir $NAME
mkdir $NAME/pdf
chmod 700 $NAME/pdf
mkdir $NAME/text
chmod 700 $NAME/text
mkdir $NAME/index
mkdir $NAME/graphs

# done
exit 0

