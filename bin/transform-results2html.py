#!/usr/bin/env python

# transform-results2html.py - given standard input, output an HTML table of search results

# Eric Lease Morgan <emorgan@nd.edu>
# July 15, 2015 - first cut; based on Hathi work


# configure
HASH     = '''{ "id": "##ID##", "shortTitle": "##SHORTTITLE##", "title": "##TITLE##", "count": "##COUNT##", "size": "##SIZE##", "tfidf": "##TFIDF##", "author": "##AUTHOR##", "journalTitle": "##JOURNALTITLE##", "volume": "##VOLUME##", "issue": "##ISSUE##", "year": "##YEAR##", "pubdate": "##PUBDATE##", "pagerange": "##PAGERANGE##", "publisher": "##PUBLISHER##", "type": "##TYPE##", "reviewedwork": "##REVIEWEDWORK##", "pdf": "##PDF##", "pages": "##PAGES##", "colors": "##COLORS##", "names": "##NAMES##", "ideas": "##IDEAS##" }, '''
TEMPLATE = './etc/template-search-results.txt'

# require
import sys
import re

# sanity check
if ( len( sys.argv ) != 2 ) | ( sys.stdin.isatty() ) :
	print "Usage: ./bin/search.py <query> <name> | " + sys.argv[ 0 ] + ' <name>'
	quit()

# get input
name = sys.argv[ 1 ]

# initialize
data = ''

# process each record
for hit in sys.stdin:

	# re-initialize
	hash = HASH
	
	# read a record, and split it into fields
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
		
	# do the substitutions
	hash = re.sub( '##ID##',           fields[  0 ],  hash )
	
	title = re.sub( '\"', '\\"',       fields[  4 ] )
	hash = re.sub( '##SHORTTITLE##',   title[:50] + '...',  hash )
	hash = re.sub( '##TITLE##',        title,  hash )
	
	hash = re.sub( '##COUNT##',        fields[  1 ],  hash )
	hash = re.sub( '##SIZE##',         fields[  2 ],  hash )
	hash = re.sub( '##TFIDF##',        fields[  3 ],  hash )
	hash = re.sub( '##AUTHOR##',       fields[  5 ],  hash )
	hash = re.sub( '##JOURNALTITLE##', fields[  6 ],  hash )
	hash = re.sub( '##VOLUME##',       fields[  7 ],  hash )
	hash = re.sub( '##ISSUE##',        fields[  8 ],  hash )
	hash = re.sub( '##YEAR##',         fields[  9 ],  hash )
	hash = re.sub( '##PUBDATE##',      fields[ 10 ],  hash )
	hash = re.sub( '##PAGERANGE##',    fields[ 11 ],  hash )
	hash = re.sub( '##PUBLISHER##',    fields[ 12 ],  hash )
	hash = re.sub( '##TYPE##',         fields[ 13 ],  hash )
	hash = re.sub( '##REVIEWEDWORK##', fields[ 14 ],  hash )
	hash = re.sub( '##PDF##',          fields[ 16 ],  hash )
	hash = re.sub( '##PAGES##',        fields[ 17 ],  hash )
	hash = re.sub( '##COLORS##',       fields[ 18 ],  hash )
	hash = re.sub( '##NAMES##',        fields[ 19 ],  hash )
	hash = re.sub( '##IDEAS##',        fields[ 20 ],  hash )

	# update the data
	data += hash

# create the html; do the substitutions
with open ( TEMPLATE ) as HTML : html = HTML.read()
html = re.sub( '##TITLE##', name, html )
html = re.sub( '##DATA##',  data, html )

# output and done
print html
quit()


