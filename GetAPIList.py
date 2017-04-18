#!/usr/bin/env python

#############################################################################################################################################
"""GetAPIList.py: Doc generator for all api tests"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Development"
#############################################################################################################################################

import re

tests_suite = [
	"tests_authentication",
	"tests_profile",
	"tests_notifications",
	"tests_loop",
	"tests_lifepage",
	"tests_uploadpost",
	"tests_lifepost",
	"tests_comment",
	"tests_follow",
	"tests_search",
	"tests_like",
	"tests_contact",
	"tests_hashtag",
	"tests_reportcontent",
]

f_out = open ("API_list.csv", 'w')

pattern1 = re.compile ("api_type\": \"(.*)\"")
pattern2 = re.compile ("api_url\": \"(.*)\"")
#pattern3 = re.compile ("Status: (.*)")
pattern3 = re.compile ("#+((.*)-\d\.(.*))")

for each_file in tests_suite:
	f_out.write (",***" + each_file + "***" + "\n")
	with open ("modules\\tests\\detailed_tests\\" + each_file + ".py") as f:
		for line in f:
			#Status
			MatchObject3 = pattern3.search (line)
			if MatchObject3:
			  #for groupItem in MatchObject3.groups(1):
			    f_out.write ("\"" + str (MatchObject3.groups(1)[0]).replace ("\"", "'").replace ("#", "").strip () + "\","),

			#api_type
			MatchObject1 = pattern1.search (line)
			if MatchObject1:
			  #for groupItem in MatchObject1.groups(1):
			    f_out.write (str (MatchObject1.groups(1)[0]).strip () + ","),
	
			#api_base_url
			MatchObject2 = pattern2.search (line)
			if MatchObject2:
			  #for groupItem in MatchObject2.groups(1):
			    f_out.write (str (MatchObject2.groups(1)[0]).strip () + "\n")
		print ("")