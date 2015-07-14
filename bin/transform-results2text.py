#!/usr/bin/env python

# results2text.py - format search results as a stream of plain text

# Eric Lease Morgan <emorgan@nd.edu>
# July 14, 2015 - first cut; based on Hathi work


# require
import sys

# sanity check
if sys.stdin.isatty() :
	print "Usage: ./bin/search.py <query> <name> | " + sys.argv[ 0 ] 
	quit()
	
# initialize
pointer = 0

# process each hit from standard input
for hit in sys.stdin:

	# increment
	pointer = pointer + 1
	
	# get a record with the following strucxture:
	#  0  key
	#  1  count
	#  2  size
	#  3  tfidf
	#  4  title
	#  5  author
	#  6  journalTitle
	#  7  volume
	#  8  issue
	#  9  year
	# 10  pubdate
	# 11  pagerange
	# 12  publisher
	# 13  type
	# 14  reviewedwork
	# 15  abstract
	# 16  pdf
	# 17  pages
	# 18  color
	# 19  names
	# 20  ideas	
	fields = hit.rstrip().split( '\t' )
	
	# output
	print( str( pointer ) + '. '   + fields[  4 ] )
	print( '             author: ' + fields[  5 ] )
	print( '           abstract: ' + fields[ 15 ] )
	print( '               year: ' + fields[  9 ] )
	print( '              tfidf: ' + fields[  3 ] )
	print( '              count: ' + fields[  1 ] )
	print( '               size: ' + fields[  2 ] )
	print( '              pages: ' + fields[ 17 ] )
	print( '          pagerange: ' + fields[ 11 ] )
	print( '       journalTitle: ' + fields[  6 ] )
	print( '             volume: ' + fields[  7 ] )
	print( '              issue: ' + fields[  8 ] )
	print( '            pubdate: ' + fields[ 10 ] )
	print( '          publisher: ' + fields[ 12 ] )
	print( '               type: ' + fields[ 13 ] )
	print( '       reviewedwork: ' + fields[ 14 ] )
	print( '             colors: ' + fields[ 18 ] )
	print( '              names: ' + fields[ 19 ] )
	print( '              ideas: ' + fields[ 20 ] )
	print( '                PDF: ' + fields[ 16 ] )
	print( '                 id: ' + fields[  0 ] )
	print

# done
quit()

