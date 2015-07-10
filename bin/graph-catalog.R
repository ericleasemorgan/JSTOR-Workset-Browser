#!/usr/bin/env Rscript

# graph-catalog.R - create a boxplot as well as a histogram illustrating the distribution of dates in the catalog

# Eric Lease Morgan <emorgan@nd.edu>
# June  7, 2015 - started using for EEBO
# June 10, 2015 - getting to work with the catalog
# June 13, 2015 - added pages


# configure
CATALOG = '/catalog.db'
GRAPHS  = '/graphs/'

# get input
name = commandArgs( trailingOnly = TRUE )

# read and parse
catalog =  read.table( paste( name, CATALOG, sep='' ), sep='\t', header=T, quote = '', fill = TRUE )
dates      <- catalog$years
pages      <- catalog$pages
words      <- catalog$sizes
colors     <- catalog$colors
names      <- catalog$names
ideas      <- catalog$ideas

# create a matrix of scatter plots
png( filename = ( paste( name, GRAPHS, 'catalog-scatterplot.png', sep='' ) ) )
pairs(~dates+pages+words+colors+names+ideas, data=catalog, main="Scatterplot Matrix")

# create boxplots and histograms for each of the numeric columns; dates
png( filename = paste( name, GRAPHS, 'catalog-boxplot-dates.png', sep='' ) )
boxplot( dates, main=( paste( 'Dates (' , name, ')', sep='' ) ) )
png( filename = paste( name, GRAPHS, 'catalog-histogram-dates.png', sep='' ) )
hist( dates, freq=FALSE, main=( paste('Dates (' , name, ')', sep='' ) ) )
curve( dnorm( x, mean=mean( dates ), sd=sd( dates ) ), add=TRUE, col="darkblue", lwd=2 )

# pages
png( filename = paste( name, GRAPHS, 'catalog-boxplot-pages.png', sep='' ) )
boxplot( pages, main=( paste( 'Pages (' , name, ')', sep='' ) ) )
png( filename = paste( name, GRAPHS, 'catalog-histogram-pages.png', sep='' ) )
hist( pages, freq=FALSE, main=( paste('Pages (' , name, ')', sep='' ) ) )

# words
png( filename = paste( name, GRAPHS, 'catalog-boxplot-words.png', sep='' ) )
boxplot( words, main=( paste( 'Sizes in words (' , name, ')', sep='' ) ) )
png( filename = paste( name, GRAPHS, 'catalog-histogram-words.png', sep='' ) )
hist( words, freq=FALSE, main=( paste('Sizes in words (' , name, ')', sep='' ) ) )
curve( dnorm( x, mean=mean( words ), sd=sd( words ) ), add=TRUE, col="darkblue", lwd=2 )

# colors
png( filename = ( paste( name, GRAPHS, 'catalog-boxplot-colors.png', sep='' ) ) )
boxplot( colors, main="Colors")
png( filename = ( paste( name, GRAPHS, 'catalog-histogram-colors.png', sep='' ) ) )
hist( colors, freq=FALSE, main="Colors")
curve( dnorm( x, mean=mean( colors ), sd=sd( colors ) ), add=TRUE, col="darkblue", lwd=2 )

# names
png( filename = ( paste( name, GRAPHS, 'catalog-boxplot-names.png', sep='' ) ) )
boxplot( names, main="'Big' names")
png( filename = ( paste( name, GRAPHS, 'catalog-histogram-names.png', sep='' ) ) )
hist( names, freq=FALSE, main="'Big' names")
curve( dnorm( x, mean=mean( names ), sd=sd( names ) ), add=TRUE, col="darkblue", lwd=2 )

# ideas
png( filename = ( paste( name, GRAPHS, 'catalog-boxplot-ideas.png', sep='' ) ) )
boxplot( ideas, main="'Great' ideas")
png( filename = ( paste( name, GRAPHS, 'catalog-histogram-ideas.png', sep='' ) ) )
hist( ideas, freq=FALSE, main="'Great' ideas")
curve( dnorm( x, mean=mean( ideas ), sd=sd( ideas ) ), add=TRUE, col="darkblue", lwd=2 )

# done
quit()
