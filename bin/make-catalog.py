#!/usr/bin/env python

# make-catalog.py - create a "catalog" from a DFR JSTOR dataset citations.xml file

# Eric Lease Morgan <emorgan@nd.edu>
# July 4, 2015 - first investigations


# configure
DEBUG     = 0
CITATIONS = '/citations.xml'

# require
import sys
import libxml2

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
	id           = article.xpathEval( './@id' )
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
	if id : id = id[ 0 ].content
	else: id = ''
	
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
	
	
	print "             id : " + id
	print "          title : " + title
	print "         author : " + author
	print "  journal title : " + journaltitle
	print "         volume : " + volume
	print "          issue : " + issue
	print "        pubdate : " + pubdate
	print "      pagerange : " + pagerange
	print "      publisher : " + publisher
	print "           type : " + type
	print "  reviewed work : " + reviewedwork
	print "       abstract : " + abstract
	print
	
quit()

