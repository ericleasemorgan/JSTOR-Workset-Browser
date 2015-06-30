#!/bin/bash

# initialize.sh - create a directory structure to hold our data

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut


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
mkdir $NAME/text
mkdir $NAME/index

# done
exit 0

