#!/usr/bin/perl

# harvest.pl - given an XML file of citations from DFR, locally cache a set of PDF documents

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut; based on jstor-tool; think about GMCC and hiding a flower


# configure
use constant COOKIES => './cookies.txt';
use constant JSTOR   => '10.2307/';
use constant MAXIMUM => 50;
use constant CACHE   => '/pdf';
use constant PDFPLUS => 'http://www.jstor.org/stable/pdfplus/##JSTORID##.pdf?acceptTC=true';

# require
use LWP::UserAgent;
use strict;
use XML::XPath;

# sanity check
if ( ! $ARGV[ 0 ] | -t STDIN ) { 

	print "Usage: cat <citations.xml> | $0 <name>\n";
	exit 1;
	
}

# initialize
my $name      = $ARGV[ 0 ];
my $citations = do { local $/; <STDIN> };
my $parser    = XML::XPath->new( xml => $citations );
my $ua        = LWP::UserAgent->new;
$ua->cookie_jar( { file => COOKIES } );
binmode( STDOUT, ':utf8' );

# process each article in the list of citations
my $index     = 0;
my $citations = $parser->find( '//article' );
foreach my $citation ( $citations->get_nodelist ) {
	
	# get the identifier
	my $prefix =  JSTOR;
	my $id     =  $citation->find( './doi' );
	$id        =~ s/$prefix//e;
	
	# create a URL
	my $url =  PDFPLUS;
	$url    =~ s/##JSTORID##/$id/e;
	
	# create the pdf filename
	my $pdf = $name . CACHE . "/$id.pdf";
	
	# get the title
	my $title = '[NO TITLE SUPPLIED]';
	if ( length( $citation->find( './title' ))) { $title = $citation->find( './title' ) }

	# echo
	print "     id: $id\n";
	print "  title: $title\n";
	print "    url: $url\n";
	print "    PDF: $pdf\n";
	print "\n";

	# increment
	$index++;
	last if ( $index > MAXIMUM );
	
	# get and save the remote pdf file
	my $request  = HTTP::Request->new( 'GET', $url );
	my $response = $ua->request( $request );
	open PDF, " > $pdf";
	print PDF $response->content;
	close PDF;

}

# done
exit 0;
