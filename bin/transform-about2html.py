#!/usr/bin/env python

# transform-about2html.py - transform an about.db file into an HTML stream

# Eric Lease Morgan <emorgan@nd.edu>
# July 15, 2015 - first cut; based on Hathi work


# configure
ABOUT    = '/about.db'
CATALOG  = '/catalog.db'
SEARCH   = './search.cgi?q='
TEMPLATE = './etc/template-about.txt'

# require
import sys
import re

# sanity check
if len( sys.argv ) != 2 :
	print "Usage: " + sys.argv[ 0 ] + ' <name>'
	quit()

# get input
corpus = sys.argv[ 1 ]

# read the database
metadata = {}
with open ( corpus + ABOUT ) as database :

		# process each record
		for record in database :
		
			# map each field to my metadata
			field = record.rstrip().split( '\t' )
			metadata[ field[ 0 ] ] = field[ 1 ]

# mark-up the frequently used words (not scalable)
frequent_links = ''
for word in metadata[ 'FREQUENTWORDS' ].rstrip( '|' ).split( '|' ) :

	fields = word.split( ' ' )
	item   = fields[ 0 ]
	count  = str( fields[ 1 ] )
	frequent_links  = frequent_links + '<a href="' + SEARCH + item + '">' + item + '</a> (' + count + ')&nbsp; '

# colors
color_links = ''
for color in metadata[ 'FREQUENTCOLORS' ].rstrip( '|' ).split( '|' ) :

	fields = color.split( ' ' )
	item   = fields[ 0 ]
	count  = str( fields[ 1 ] )
	color_links  = color_links + '<a href="' + SEARCH + item + '">' + item + '</a> (' + count + ')&nbsp; '

# names
names_links = ''
for name in metadata[ 'FREQUENTNAMES' ].rstrip( '|' ).split( '|' ) :

	fields = name.split( ' ' )
	item   = fields[ 0 ]
	count  = str( fields[ 1 ] )
	names_links  = names_links + '<a href="' + SEARCH + item + '">' + item + '</a> (' + count + ')&nbsp; '

# ideas
ideas_links = ''
for idea in metadata[ 'FREQUENTIDEAS' ].rstrip( '|' ).split( '|' ) :

	fields = idea.split( ' ' )
	item   = fields[ 0 ]
	count  = str( fields[ 1 ] )
	ideas_links  = ideas_links + '<a href="' + SEARCH + item + '">' + item + '</a> (' + count + ')&nbsp; '

# look up keys in catalog and get metadata
catalog = {}
with open ( corpus + CATALOG ) as database :

	index = 0
	for record in database :
	
		# increment and check; we don't need the catalog's header
		index = index + 1
		if index == 1 : continue
		
		# remember, the fields in the (default) catalog
		#   0 ids
		#   1 fkeys
		#   2 titles
		#   3 authors
		#   4 journaltitltes
		#   5 volumes
		#   6 issues
		#   7 years
		#   8 pubdates
		#   9 pageranges
		#  10 publishers
		#  11 types
		#  12 reveiwedworks
		#  13 abstracts
		#  14 pdfs
		#  15 pages
		#  16 sizes
		#  17 colors
		#  18 names
		#  19 ideas		
		fields = record.rstrip().split( '\t' )

		# get the key
		key = fields[ 0 ]
				
		catalog[ key ] = {}
		catalog[ key ][ 'title' ] = fields[  2 ]
		catalog[ key ][ 'pdf' ]   = fields[ 14 ]

# create the links of interest; shortest
title        = catalog[ metadata[ 'WORKSHORTEST' ] ][ 'title' ]
pdf          = '<a href="' + catalog[ metadata[ 'WORKSHORTEST' ] ][ 'pdf' ] + '">PDF</a>'
workshortest = title + ' (' + pdf + ')'

# longest
title       = catalog[ metadata[ 'WORKLONGEST' ] ][ 'title' ]
pdf         = '<a href="' + catalog[ metadata[ 'WORKLONGEST' ] ][ 'pdf' ] + '">PDF</a>'
worklongest = title + ' (' + pdf + ')'

# oldest
title      = catalog[ metadata[ 'WORKOLDEST' ] ][ 'title' ]
pdf        = '<a href="' + catalog[ metadata[ 'WORKOLDEST' ] ][ 'pdf' ] + '">PDF</a>'
workoldest = title + ' (' + pdf + ')'

# newest
title      = catalog[ metadata[ 'WORKNEWEST' ] ][ 'title' ]
pdf        = '<a href="' + catalog[ metadata[ 'WORKNEWEST' ] ][ 'pdf' ] + '">PDF</a>'
worknewest = title + ' (' + pdf + ')'

# most ideas
title     = catalog[ metadata[ 'IDEASMOST' ] ][ 'title' ]
pdf       = '<a href="' + catalog[ metadata[ 'IDEASMOST' ] ][ 'pdf' ] + '">PDF</a>'
ideasmost = title + ' (' + pdf + ')'

# least ideas
title      = catalog[ metadata[ 'IDEASLEAST' ] ][ 'title' ]
pdf        = '<a href="' + catalog[ metadata[ 'IDEASLEAST' ] ][ 'pdf' ] + '">PDF</a>'
ideasleast = title + ' (' + pdf + ')'

# most names
title     = catalog[ metadata[ 'NAMESMOST' ] ][ 'title' ]
pdf       = '<a href="' + catalog[ metadata[ 'NAMESMOST' ] ][ 'pdf' ] + '">PDF</a>'
namesmost = title + ' (' + pdf + ')'

# least names
title      = catalog[ metadata[ 'NAMESLEAST' ] ][ 'title' ]
pdf        = '<a href="' + catalog[ metadata[ 'NAMESLEAST' ] ][ 'pdf' ] + '">PDF</a>'
namesleast = title + ' (' + pdf + ')'

# most colors
title      = catalog[ metadata[ 'COLORSMOST' ] ][ 'title' ]
pdf        = '<a href="' + catalog[ metadata[ 'COLORSMOST' ] ][ 'pdf' ] + '">PDF</a>'
colorsmost = title + ' (' + pdf + ')'

# least colors
title       = catalog[ metadata[ 'COLORSLEAST' ] ][ 'title' ]
pdf         = '<a href="' + catalog[ metadata[ 'COLORSLEAST' ] ][ 'pdf' ] + '">PDF</a>'
colorsleast = title + ' (' + pdf + ')'

# do some math; add more "kewl" calculations here
pagesaverage = str( int( metadata[ 'PAGESTOTAL' ] ) / int( metadata[ 'CORPUSSIZE' ] ) )
wordsaverage = str( int( metadata[ 'WORDSTOTAL' ] ) / int( metadata[ 'CORPUSSIZE' ] ) )

# slurp up the template; find & replace the tokesn
with open ( TEMPLATE ) as HTML : html = HTML.read()
html = re.sub( '##CORPUSNAME##',     metadata[ 'CORPUSNAME' ],    html )
html = re.sub( '##CORPUSSIZE##',     metadata[ 'CORPUSSIZE' ],    html )
html = re.sub( '##DATEEARLIEST##',   metadata[ 'DATEEARLIEST' ],  html )
html = re.sub( '##DATELATEST##',     metadata[ 'DATELATEST' ],    html )
html = re.sub( '##PAGESSHORTEST##',  metadata[ 'PAGESSHORTEST' ], html )
html = re.sub( '##PAGESLONGEST##',   metadata[ 'PAGESLONGEST' ],  html )
html = re.sub( '##PAGESTOTAL##',     metadata[ 'PAGESTOTAL' ],    html )
html = re.sub( '##PAGESAVERAGE##',   pagesaverage,                html )
html = re.sub( '##WORDSSHORTEST##',  metadata[ 'WORDSSHORTEST' ], html )
html = re.sub( '##WORDSLONGEST##',   metadata[ 'WORDSLONGEST' ],  html )
html = re.sub( '##WORDSTOTAL##',     metadata[ 'WORDSTOTAL' ],    html )
html = re.sub( '##WORDSAVERAGE##',   wordsaverage,                html )
html = re.sub( '##WORDSUNIQUE##',    metadata[ 'WORDSUNIQUE' ],   html )
html = re.sub( '##FREQUENTWORDS##',  frequent_links,              html )
html = re.sub( '##FREQUENTIDEAS##',  ideas_links,                 html )
html = re.sub( '##FREQUENTNAMES##',  names_links,                 html )
html = re.sub( '##FREQUENTCOLORS##', color_links,                 html )
html = re.sub( '##WORKSHORTEST##',   workshortest,                html )
html = re.sub( '##WORKLONGEST##',    worklongest,                 html )
html = re.sub( '##WORKOLDEST##',     workoldest,                  html )
html = re.sub( '##WORKNEWEST##',     worknewest,                  html )
html = re.sub( '##IDEASMOST##',      ideasmost,                   html )
html = re.sub( '##IDEASLEAST##',     ideasleast,                  html )
html = re.sub( '##NAMESMOST##',      namesmost,                   html )
html = re.sub( '##NAMESLEAST##',     namesleast,                  html )
html = re.sub( '##COLORSMOST##',     colorsmost,                  html )
html = re.sub( '##COLORSLEAST##',    colorsleast,                 html )

# output and done
print html
quit()


