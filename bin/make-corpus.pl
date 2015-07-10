#!/usr/bin/perl

# make-corpus.pl - given an XML file of citations from DFR, locally cache a set of PDF documents

# Eric Lease Morgan <emorgan@nd.edu>
# June 30, 2015 - first cut; based on jstor-tool; think about GMCC and hiding a flower
# July  6, 2015 - cached STDIN to citations.xml for later processing
# July  9, 2015 - removed the removal of the doi prefix; added user-agent identifiers


# configure
use constant FROM      => 'emorgan@nd.edu';
use constant AGENT     => 'JSTOR-Workset-Browser/0.1 ';
use constant COOKIES   => './cookies.txt';
use constant MAXIMUM   => 1000;
use constant CACHE     => '/pdf';
use constant PDFPLUS   => 'http://www.jstor.org/stable/pdfplus/##JSTORID##.pdf?acceptTC=true';
use constant CITATIONS => '/citations.xml';

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

# cache the citations to a file for later processing
open XML, " > $name" . CITATIONS or die "Can't open citations.xml: $!\n";
print XML $citations;
close XML;

# continue initialization
my $parser  = XML::XPath->new( xml => $citations );
my $ua      = LWP::UserAgent->new;
$ua->agent( AGENT );
$ua->from( FROM );
$ua->cookie_jar( { file => COOKIES } );
binmode( STDOUT, ':utf8' );

# process each article in the list of citations
my $index     = 0;
my $citations = $parser->find( '//article' );
foreach my $citation ( $citations->get_nodelist ) {
	
	# get the identifier
	my $id = $citation->find( './doi' );
	
	# create a URL
	my $url =  PDFPLUS;
	$url    =~ s/##JSTORID##/$id/e;
	
	# create the pdf filename
	my $pdf =  $id;
	$pdf    =~ s/\./_/g;
	$pdf    =~ s/\//-/g;
	$pdf    =  $name . CACHE . "/$pdf.pdf";
	
	# get the title
	my $title = '[NO TITLE SUPPLIED]';
	if ( length( $citation->find( './title' ))) { $title = $citation->find( './title' ) }

	# echo
	print "  index: $index\n";
	print "     id: $id\n";
	print "  title: $title\n";
	print "    url: $url\n";
	print "    PDF: $pdf\n";
	print "\n";
	
	# get the PDF file, if necessary
	if ( ! -e $pdf ) {
	
		# get and save the remote pdf file
		my $request  = HTTP::Request->new( 'GET', $url );
		my $response = $ua->request( $request );
		open PDF, " > $pdf";
		print PDF $response->content;
		close PDF;
	
		# increment
		$index++;
		last if ( $index > MAXIMUM );

	}

}

# done
exit 0;
