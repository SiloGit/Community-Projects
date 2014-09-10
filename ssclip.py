#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
#	SiloSec presents - 
#	Our first community project
#	Name pending. 

"""
	Objective:

	Scrape info from a wiki, organize them, and
	then post them to Quizlet as flash cards.

	Cards -
	Wiki -
	Twitter - @Soul_Protocol

"""

__authors__ = "Jay (SiloSec) (j@silosec.org), jsrn - #slothkrew"
__version__ = "0.1a"
__date__ = "Date: Sep 10, 2014"
__more_info__ = "http://www.silosec.org"


### Imports ----
import urllib3 #or...
from mechanize import Browser		# Fetches info for BSoup
import re 							# Regular Expressions - Used here to organize strings
import sys							# For Command-Line Arguments and Script Exit
from bs4 import BeautifulSoup		# Does the heavy lifting in the scraping department


### Variables ----

# Pretty colors are Pretty
W  = '\033[0m'  # white
G  = '\033[32m' # green
R  = '\033[31m' # red
B  = '\033[34m' # blue
P  = '\033[35m' # purple
GR = '\033[37m' # gray

fcurl = "http://quizlet.com/44970397/linux-and-hacking-common-commands-and-memorize-mes-flash-cards/"  # Location of the Quizlet Flash Cards

mech = Browser()					    # Using Mechanize to fetch html
page = mech.open(fcurl)				# Assigning the fetched page
html = page.read()				  	# HTML Content ready for BS
wurl = ""						        	# Wiki's URL
							
version = "0.1a"				    	# Script Version Number



### Main ----

# Help menu
def usage():
    print G+'[!] ssclip ' + version + ' by '+B+' Silo Collective'
    print P+"Usage: ssclip <options>\n"
    print "Options:"
    print "-h -- Print this help message."
    print ""

usage()

if __name__ == "__main__":
        try:
			main()
	except KeyboardInterrupt:
		print B+"Search interrupted by user.."
		#exit_gracefully(0)
	except:
		#exit_gracefully(0)
		sys.exit


