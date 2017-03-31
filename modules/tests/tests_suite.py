#!/usr/bin/env python

#############################################################################################################################################
"""tests_suite.py: This is the test suite configuration."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

global_dict = {
	"running": False,
	"server":"http://dev.media.jio.com/n18/",
	#"server":"https://api.stackexchange.com/2.2/",
	#"server":"http://api-beta.wally.me/",
	"headers": {
		"appkey":"bjzLHR11aEvXwIk0pF0x",
		"deviceid": "q1l1fULw5ddj8ysCkDJ8",
		"usergroup":"q1l1fULw5ddj8ysCkDJ8",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
	},
}

run_list = ['POST', 'GET']

tests_suite = [
	"Network18.tests_apphomekey",
	#"Network18.tests_comment",
	#"Network18.tests_pancake",
	#"Wally.tests_token",
	#"Misc.tests_misc",
]