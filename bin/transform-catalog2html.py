#!/usr/bin/env python

# transform-catalog2html.py - given the name of a corpus, output a human-readable version of the corpus's catalog

# Eric Lease Morgan <emorgan@nd.edu>
# July 11, 2015 - first cut; based on EEBO-TCP work


# configure
CATALOG  = '/catalog.db'
HASH     = '''{ "id": "##ID##", "fkey": "##FKEY##", "shortTitle": "##SHORTTITLE##", "title": "##TITLE##", "author": "##AUTHOR##", "journalTitle": "##JOURNALTITLE##", "volume": "##VOLUME##", "issue": "##ISSUE##", "year": "##YEAR##", "pubdate": "##PUBDATE##", "pageRange": "##PAGERANGE##", "publisher": "##PUBLISHER##", "type": "##TYPE##", "reviewedWork": "REVIEWEDWORK", "pdf": "##PDF##", "pages": "##PAGES##", "words": "##WORDS##", "colors": "##COLORS##", "names": "##NAMES##", "ideas": "##IDEAS##" }, '''
TEMPLATE = './etc/template-catalog.txt'
LENGTH   = 50

# require
import sys
import re

# sanity check
if len( sys.argv ) != 2 :
	print "Usage:", sys.argv[ 0 ], '<name>'
	quit()

# get input
name = sys.argv[ 1 ]

# open the database
data  = ''
with open( name + CATALOG ) as database :

	# initialize
	index = 0

	# process each record
	for record in database :

		# increment and re-initialize
		index += 1
		hash  =  HASH
		
		# read a record, and split it into fields
		fields = record.rstrip().split( '\t' )
		
		# check for header
		if index == 1 : continue
		
		# process the data
		else :
		
			# do the substitutions
			hash = re.sub( '##ID##',           fields[ 0 ],  hash )
			hash = re.sub( '##FKEY##',         fields[ 1 ],  hash )
			
			title = re.sub( '\"', '\\"',        fields[ 2 ] )
			hash  = re.sub( '##SHORTTITLE##',   title[:LENGTH] + '...',  hash )
			hash  = re.sub( '##TITLE##',        title,        hash )
			
			hash  = re.sub( '##AUTHOR##',       fields[  3 ], hash )
			hash  = re.sub( '##JOURNALTITLE##', fields[  4 ], hash )
			hash  = re.sub( '##VOLUME##',       fields[  5 ], hash )
			hash  = re.sub( '##ISSUE##',        fields[  6 ], hash )
			hash  = re.sub( '##YEAR##',         fields[  7 ], hash )
			hash  = re.sub( '##PUBDATE##',      fields[  8 ], hash )
			hash  = re.sub( '##PAGERANGE##',    fields[  9 ], hash )
			hash  = re.sub( '##PUBLISHER##',    fields[ 10 ], hash )
			hash  = re.sub( '##TYPE##',         fields[ 11 ], hash )
			hash  = re.sub( '##REVIEWEDWORK##', fields[ 12 ], hash )
			hash  = re.sub( '##PDF##',          fields[ 14 ], hash )
			hash  = re.sub( '##PAGES##',        fields[ 15 ], hash )
			hash  = re.sub( '##WORDS##',        fields[ 16 ], hash )
			hash  = re.sub( '##COLORS##',       fields[ 17 ], hash )
			hash  = re.sub( '##NAMES##',        fields[ 18 ], hash )
			hash  = re.sub( '##IDEAS##',        fields[ 19 ], hash )
			
		# update the data
		data += hash
		
# create the html; do the substitutions
with open ( TEMPLATE ) as HTML : html = HTML.read()
html = re.sub( '##TITLE##', name, html )
html = re.sub( '##DATA##',  data, html )

# output and done
print html
quit()


