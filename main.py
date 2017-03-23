#!/usr/bin/env python

#############################################################################################################################################
"""main.py: This is the controller.  Execution starts from here"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Moolya Software Testing"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "anand.iyer@moolya.com"
__status__ = "Production"
#############################################################################################################################################

import requests
import ast
import json
import re
import sys
import traceback

from importlib import import_module
from modules.tests.tests_suite import *
from modules.libraries.verification import *
from modules.libraries.api_object import *

global_dict["debuglog"] = open(global_dict["debuglog"] + "debuglog.txt",'w')
global_dict["reslog"]  = open(global_dict["reslog"] + "passfaillog.csv",'a')

report_start ()

for tests in tests_suite:
	subfolder = ""
	tests_in_folder = tests.split ('.')

	#import only the required list of tests; contained in test_list
	mod = import_module ("modules.tests." + tests)
	if len(tests_in_folder) > 1:
		for folder in tests_in_folder[:-1]:
			subfolder += "\\" + folder
		tests = tests_in_folder[-1]
		subfolder += "\\"
	
	test_list = getattr (mod, tests)
	
	for test in test_list:
		current_api = api_object(test)
		
		#Execute only the api_types in run_list (tests_suite.py)
		if not current_api.api_type in run_list:
			continue
		
		#substitute for api_store
		try:
			api_store = current_api.api_store
			for each_key in current_api.keys():
				if each_key == "api_store":
					continue
				
				if isinstance (current_api[each_key], dict):
					for each_subkey in current_api[each_key].keys():
						if isinstance (current_api[each_key][each_subkey], int):
							continue
						
						#Replace anything between <> from global_dict                       
						matches = re.findall ("<(.*?)>", current_api[each_key][each_subkey], re.DOTALL)
						for match in matches:
							current_api[each_key][each_subkey] = re.sub('<' + match + '>',global_dict[match], current_api[each_key][each_subkey])
						
						# if current_api[each_key][each_subkey] != "":
						#   current_api[each_key][each_subkey] = json.loads (current_api[each_key][each_subkey])
				else:
					#Replace anything between <> from global_dict                       
					matches = re.findall("<(.*?)>", current_api[each_key], re.DOTALL)
					for match in matches:
						current_api[each_key] = re.sub('<' + match + '>',global_dict[match], current_api[each_key])

					# if current_api[each_key][each_subkey] != "":
					#   current_api[each_key][each_subkey] = json.loads (current_api[each_key][each_subkey])
		except:
			traceback.print_exc (file=global_dict["debuglog"]) #api_store may not be present

		#Store object attributes temporarily, before using them
		api_url = current_api.api_url
		api_type = current_api.api_type
		api_name = current_api.api_name
		api_function = current_api.api_function
		api_params = current_api.api_params
		api_headers = current_api.api_headers
		api_expected = current_api.api_expected
		output_mode = current_api.output_mode
		
		#substituting for the api_repl
		try:
			url_placeholders = current_api.api_repl
			for each in url_placeholders:
				matchIt = re.compile ("{" + each + "}")
				if url_placeholders[each] == "global_dict":
					repl = global_dict[each]
				else:
					repl = url_placeholders[each]
				api_url = matchIt.sub(repl, api_url)
				
			current_api.api_url = api_url #replace in the api_object
		except:
			pass #api_repl may not be present
		
		#construct URL
		if api_type == "GET" or api_type == "DELETE":
			api_params_set = "?"
			for param in api_params.keys():
				api_params_set = api_params_set + param + "=" + api_params[param] + "&"
			
			api_url = (api_url + api_params_set)[:-1]

		#get the function pointer
		mod = import_module ("modules.libraries.api_functions")
		function_to_call = getattr (mod, api_function)

		try:
			result = False
			#get the server response
	
			if api_type == "POST":
				#global_dict["headers"].update ({'Content-type': 'application/json', 'Accept': 'application/json'})
				req = requests.post (api_url, data = json.dumps (api_params), headers=global_dict["headers"])
				current_api.data = req.text
				current_api.status_code = req.status_code
	
			actuals_folder = global_dict["actuals_folder"] + subfolder + "actuals\\" + api_name #re-using for writing the reports.
			current_api.actuals_folder = actuals_folder
			
			report_it ("datetime",
				   subfolder + tests + "\\" + api_name, api_url, api_type)

			#Parse the response, and verify the results
			if not (api_type == "DELETE"):
				if function_to_call is not None:
					result = function_to_call (current_api)
				else:
					result = True
			else:
				result = True #assume that it passed
		except Exception: #so, you can continue with the next test
			traceback.print_exc (file=global_dict["debuglog"])

		report_it (bool (result))
			
global_dict["debuglog"].close()
global_dict["reslog"].close()