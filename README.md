# JSTOR-Workset-Browser

Given a citations.xml file, this suite of files will cache and index content identified through JSTOR's Data For Research service. The resulting (and fledgling) reports created by this suite enables the reader to "read distantly" against a collection of journal articles. 

The suite requires a hodgepodge of software: Perl, Python, and the Bash Shell. Your milage may vary.

Sample usage: `cat etc/citations-thoreau.xml | bin/make-everything.sh thoreau`
	
This software is distributed under the GNU Public License.

"Release early. Release often".

Eric Lease Morgan <emorgan@nd.edu>

June 30, 2015