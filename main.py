#!/usr/bin/env python

#############################################################################################################################################
"""main.py: This is the controller.  Execution starts from here"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

import requests
import ast
import json
import re
import sys
import traceback

from importlib import import_module
from modules.libraries.verification import *
from modules.libraries.api_object import *
from modules.tests.tests_suite import *
from os import path

def main_config (run_from_web, username=""):
	global_dict["tests"] = [] #contains the same set of tests globally, so that it can be accesssed by web pages.

	tests_folder_name = "tests_%s" %(username)
	tests_folder = "%s/modules/%s" %(path.dirname(path.abspath(__file__)), tests_folder_name)
	tests_modules_name = "modules.%s." %(tests_folder_name)

	test_list = []
	for test_category in tests_suite:
		subfolder = ""
		tests_in_folder = test_category.split ('.')
	
		#import only the required list of tests; contained in test_list
		try:
			mod = import_module (tests_modules_name + test_category)
		
			if len(tests_in_folder) > 1:
				for folder in tests_in_folder[:-1]:
					subfolder += "\\" + folder
			test_list = getattr (mod, tests_in_folder[-1]) #tests_in_folder[-1] is tests_user_defined
			test_category = folder + "." + tests_in_folder[-1] #Misc.tests_user_defined
		except:
			pass
		
		
		for test in test_list:
			test["api_category"] = test_category 
			folder_parts = (tests_folder + "\\" + test["api_category"]).replace ('.','\\').split ('\\')
			folder = '\\'.join (folder_parts[:-1]) #tests folder
			filename = folder_parts[-1] + ".py" #only the filename.
			test["api_download"] = "download?folder=%s&filename=%s" %(folder, filename) #download tests
			global_dict["tests"].append ((test, test_category, subfolder.strip ('\\')))
	
	if run_from_web: #if found running from the web
		global_dict["debuglog"] = tests_folder + "\\debuglog\\"
		global_dict["reslog"] = tests_folder + "\\"
		global_dict["schema_folder"] = tests_folder + "\\schema\\"
		global_dict["test_module"] = tests_modules_name
		global_dict["test_folder"] = tests_folder + "\\"
		global_dict["run_selected"] = []
	else:
		tests_folder = tests_modules_name.replace ('.', "\\") #not full path of tests_folder
		global_dict["debuglog"] = tests_folder + "debuglog\\"
		global_dict["reslog"] = tests_folder
		global_dict["schema_folder"] = tests_folder + "schema\\"
		global_dict["test_module"] = tests_modules_name
		global_dict["test_folder"] = tests_folder
		global_dict["run_selected"] = global_dict["tests"]

	return global_dict
		
def main_driver (run_from_web, username=""):
	if not run_from_web:
		main_config (False, username)

	report_start ()
	
	for test in global_dict["run_selected"]:
		current_api = api_object(test[0]) #test[0] indicates the actual test
		test_category = test[1] #test category
		subfolder = test[2] #subfolder
		
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
						if not isinstance (current_api[each_key][each_subkey], str):
							continue
						
						#Replace anything between <> from global_dict                       
						matches = re.findall ("<(.*?)>", current_api[each_key][each_subkey], re.DOTALL)
						for match in matches:
							current_api[each_key][each_subkey] = re.sub('<' + match + '>',global_dict[match], current_api[each_key][each_subkey])
				else:
					#Replace anything between <> from global_dict                       
					matches = re.findall("<(.*?)>", current_api[each_key], re.DOTALL)
					for match in matches:
						current_api[each_key] = re.sub('<' + match + '>',global_dict[match], current_api[each_key])
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

		#define headers for the api
		headers = {}
		headers.update (api_headers)
		
		#get the function pointer
		mod = import_module ("modules.libraries.api_functions")
		function_to_call = getattr (mod, api_function)

		try:
			result = False
			#get the server response
			if api_type == "GET":
				response = requests.get (api_url, headers=headers)
			
			if api_type == "DELETE":
				api_name = api_name + "_delete" #distinguish the .csv filename for DELETE calls
				response = requests.delete (api_url)
			
			if api_type == "PUT":
				api_name = api_name + "_put" #distinguish the .csv filename for PUT calls
				global_dict["headers"].update ({'Content-type': 'application/json', 'Accept': 'application/json'})
				response = requests.put (api_url, data = json.dumps (api_params), headers=headers)
			
			if api_type == "POST":
				global_dict["headers"].update ({'Content-type': 'application/json', 'Accept': 'application/json'})
				response = requests.post (api_url, data = json.dumps (api_params), headers=headers)

			current_api.data = response.text
			current_api.status_code = response.status_code
	
			actuals_folder = "%s%s\\%s\\" %(global_dict["test_folder"], subfolder, "actuals") #re-using for writing the reports.
			current_api.actuals_folder = actuals_folder

			report_it ("datetime",
				   test="%s\\%s" %(test_category.replace ('.', '\\'), api_name),
				   api_url=api_url,
				   api_type=api_type)
			
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

		report_it (bool (result),
				   api_expected=api_expected)
				
	try:
		global_dict["debuglog"].close()
		global_dict["reslog"].close()
		global_dict["schema"].close()
	except:
		pass
#main program
if __name__ == '__main__':
	main_config (False, username="anand")
	main_driver (False, username="anand")