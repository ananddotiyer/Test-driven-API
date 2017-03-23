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
	"session_id":"", "ipaddress":"127.0.0.1",
	"server":"https://staging.vxwb.in",
	"headers": {
		"Content-Type": "application/json"
	},
	"actuals_folder": "modules\\tests\\",
	"debuglog": "modules\\tests\\",
	"reslog": "modules\\tests\\"
}

run_list = ['POST']

tests_suite = [
	#"detailed_tests.tests_authentication",
	#"detailed_tests.tests_profile",
	#"detailed_tests.tests_notifications",
	#"detailed_tests.tests_loop",
	#"detailed_tests.tests_lifepage",
	#"detailed_tests.tests_uploadpost",
	#"detailed_tests.tests_lifepost",
	#"detailed_tests.tests_comment",
	#"detailed_tests.tests_follow",
	"detailed_tests.tests_search",
	#"detailed_tests.tests_like",
	#"detailed_tests.tests_contact",
	#"detailed_tests.tests_hashtag",
	#"detailed_tests.tests_reportcontent",
]