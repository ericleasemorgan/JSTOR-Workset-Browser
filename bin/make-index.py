#!/usr/bin/env python

# make-index.py - read plain text files and create an index of them

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first investigations; based on EEBO work


# configure
STOPWORDS = './etc/stopwords-en.txt'

# require
import operator
import re
import sys

# sanity check
if ( ( sys.stdin.isatty() ) ) :
	print "Usage: cat <text> |", sys.argv[ 0 ]
	quit()

# read and normalize the text
text = sys.stdin.read()
text = re.sub( '\s+', ' ', text )
text = text.lower()
text = text.split()

# initialize output
words = {}

# create a list of (English) stopwords
stopwords = {}
with open ( STOPWORDS ) as DATABASE :
	for record in DATABASE : stopwords[ record.rstrip() ] = 1

# process each word in the text
for word in text :
		
	# normalize some more; probably not 100% accurate
	word = word.rstrip( '?:!.,;)' )
	word = word.lstrip( '?:!.,;(' )
	
	# filter out unwanted words
	if len( word ) < 2           : continue
	if re.match( '\d|\W', word ) : continue
	if word in stopwords         : continue
	
	# update the dictionary
	words[ word ] = words.get( word, 0 ) + 1
	
# sort the list of words and output
for tuple in sorted( words.items(), key=operator.itemgetter( 1 ), reverse=True ) :
	print( tuple[ 0 ] + '\t' + str( tuple[ 1 ] ) )

# done
quit()


