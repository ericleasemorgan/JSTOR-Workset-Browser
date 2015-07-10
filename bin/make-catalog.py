#!/usr/bin/env python

# make-catalog.py - create a "catalog" from a DFR JSTOR dataset citations.xml file

# Eric Lease Morgan <emorgan@nd.edu>
# July  4, 2015 - first investigations
# July  9, 2015 - first real output
# July 10, 2015 - lost timezone in pubdate, and created a year


# configure
DEBUG     = 0
CITATIONS = '/citations.xml'
PDFPLUS   = 'http://www.jstor.org/stable/pdfplus/##JSTORID##.pdf?acceptTC=true'

# require
import sys
import libxml2
import re

# sanity check
if len( sys.argv ) != 2 :
	print sys.argv[ 0 ], '<name>'
	quit()

# get input
name = sys.argv[ 1 ]

# open the citations
citations = libxml2.parseFile( name + CITATIONS )

# process each article in the citations file
articles = citations.xpathEval( '//article')
for article in articles :

	# parse
	fkey         = article.xpathEval( './@id' )
	title        = article.xpathEval( 'title/text()' )
	author       = article.xpathEval( 'author/text()' )
	journaltitle = article.xpathEval( 'journaltitle/text()' )
	volume       = article.xpathEval( 'volume/text()' )
	issue        = article.xpathEval( 'issue/text()' )
	pubdate      = article.xpathEval( 'pubdate/text()' )
	pagerange    = article.xpathEval( 'pagerange/text()' )
	publisher    = article.xpathEval( 'publisher/text()' )
	type         = article.xpathEval( 'type/text()' )
	reviewedwork = article.xpathEval( 'reviewed-work/text()' )
	abstract     = article.xpathEval( 'abstract/text()' )

	# check and stringify
	if fkey : fkey = fkey[ 0 ].content
	else: fkey = ''
	
	if title : title = title[ 0 ].content
	else: title = ''
	
	if author : author = author[ 0 ].content
	else: author = ''
	
	if journaltitle : journaltitle = journaltitle[ 0 ].content
	else : journaltitle = ''
	
	if volume : volume = volume[ 0 ].content
	else : volume = ''

	if issue :	issue = issue[ 0 ].content
	else : issue = ''
	
	if pubdate : pubdate = pubdate[ 0 ].content
	else : pubdate = ''
	
	if pagerange : pagerange = pagerange[ 0 ].content
	else : pagerange = ''

	if publisher : publisher = publisher[ 0 ].content
	else : publisher = ''
	
	if type : type = type[ 0 ].content
	else : type = ''
	
	if reviewedwork : reviewedwork = reviewedwork[ 0 ].content
	else : reviewedwork = ''
	
	if abstract : abstract = abstract[ 0 ].content
	else : abstract = ''
		
	# create a URL to the PDF document
	pdf = re.sub( '##JSTORID##', fkey, PDFPLUS )
	
	# create a local key akin to the locally saved pdf file names
	id = re.sub( '\.', '_' , fkey )
	id = re.sub( '\/', '-' , id )
	
	# munge the pubdate; we don't need timezones
	pubdate = pubdate[:10]

	# create a year, because all of my other sets use year
	year = pubdate[:4]

	# debug
	if DEBUG :

		print "             id : " + id
		print "           fkey : " + fkey
		print "          title : " + title
		print "         author : " + author
		print "  journal title : " + journaltitle
		print "         volume : " + volume
		print "          issue : " + issue
		print "        pubdate : " + pubdate
		print "           year : " + year
		print "      pagerange : " + pagerange
		print "      publisher : " + publisher
		print "           type : " + type
		print "  reviewed work : " + reviewedwork
		print "       abstract : " + abstract
		print "            PDF : " + pdf
		print
	
	# or not; output
	else : print( '\t'.join( map( str, [ id, fkey, title, author, journaltitle, volume, issue, year, pubdate, pagerange, publisher, type, reviewedwork, abstract, pdf ] ) ) )

# done
quit()

