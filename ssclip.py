#!/usr/bin/python
#
# -*- coding: utf-8 -*-
#
#	SiloSec presents - 
#	Our first community project 

"""
                                                                              
d888888b d8b   db d88888b  .d88b.  .d8888. d88888b  .o88b. 
  `88'   888o  88 88'     .8P  Y8. 88'  YP 88'     d8P  Y8 
   88    88V8o 88 88ooo   88    88 `8bo.   88ooooo 8P      
   88    88 V8o88 88~~~   88    88   `Y8b. 88~~~~~ 8b      
  .88.   88  V888 88      `8b  d8' db   8D 88.     Y8b  d8 
Y888888P VP   V8P YP       `Y88P'  `8888Y' Y88888P  `Y88P' 
    ______ _           _                       _     
   |  ____| |         | |                     | |    
   | |__  | | __ _ ___| |__   ___ __ _ _ __ __| |___ 
   |  __| | |/ _` / __| '_ \ / __/ _` | '__/ _` / __|
   | |    | | (_| \__ \ | | | (_| (_| | | | (_| \__ \
   |_|    |_|\__,_|___/_| |_|\___\__,_|_|  \__,_|___/
                                                                                                            
                                                           	
	Objective:

	Scrape info from a wiki, organize data, and
	then post them to Quizlet as flash cards.

	Cards - http://bit.ly/1zo7rTh
	Wiki - http://www.silosec.org/w
	Twitter - @Soul_Protocol

	To Do -
	
	* Add HMAC for overkill safety and integrity check
	* 


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
import os
import getpass


### Variables ----

# Pretty colors are Pretty
W  = '\033[0m'  # white
G  = '\033[32m' # green
R  = '\033[31m' # red
B  = '\033[34m' # blue
P  = '\033[35m' # purple
GR = '\033[37m' # gray

fcurl = "http://quizlet.com/44970397/linux-and-hacking-common-commands-and-memorize-mes-flash-cards/"  # Location of the Quizlet Flash Cards

mech = Browser()					# Using Mechanize to fetch html
page = mech.open(fcurl)				# Assigning the fetched page
html = page.read()					# HTML Content ready for BS
wurl = ""							# Wiki's URL

user = raw_input("Enter Account Username: ")
pwd = getpass.getpass("Enter Account password: ")
							
version = "0.1a"					# Script Version Number



### Main ----

print("\x1B]0;---InfoSec Flashcards--- \x07")	# Print to Terminal Title Bar

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
		#print("\x1B]0;\x07")					# Change Terminal Title Bar back to Normal
		#exit_gracefully(0)
	except:
		#print("\x1B]0;\x07")					# Change Terminal Title Bar back to Normal
		#exit_gracefully(0)
		sys.exit


