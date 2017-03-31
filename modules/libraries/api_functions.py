#!/usr/bin/env python

#############################################################################################################################################
"""api_functions.py: Parsing api responses, verification of responses against expected output."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from ..export.export_apphomekey import *
from ..export.export_misc import *
from verification import *
from ..tests.tests_suite import *
from base64 import b64encode
import json
import codecs

################################################generic api function#################################################
def api_export (current_api):
	filename = current_api.actuals_folder
	expected = current_api.api_expected
	data_org = current_api.data
	response_json = current_api.response_json
	output_mode = current_api.output_mode
	status_code = current_api.status_code

	if output_mode != 'n':
		if output_mode == 'h':
			output_mode = 'a'
		f = codecs.open(filename + ".csv", output_mode,encoding='utf-16')
	else:
		f = None
	
	data_dict = json.loads (data_org)

	rowCount = 0

	result = check_status_code (status_code, expected["should_fail"])
	
	if status_code == 200:
		if response_json == "write":
			schema = get_response_schema (data_org, filename + ".json")
				
		if response_json == "match":
			schema_object = create_schema_object (filename + ".json")
			full_match_output = full_match_schema (data_org, schema_object)
			print full_match_output
			global_dict["debuglog"].write (full_match_output + "\n")
		
		if not expected["specific"]:
			if expected["row_json_path"] != "":
				jsonpath_expr = parse(expected["row_json_path"])
				write_data_dict = [match.value for match in jsonpath_expr.find(data_dict)]
				#above match gives a list with an embedded list, containing all items;
				#this means, we need to get the first item in the list, before we can access its contents
				if len (write_data_dict) == 1:
					write_data_dict = write_data_dict[0]
			else:
				write_data_dict = []
				write_data_dict.append (data_dict)
			
			rowCount = len (write_data_dict)
			result = result and WriteRow (f, write_data_dict, current_api)

			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

################################################app_homekey##############################################################
def apphomekeyslug(current_api):
	filename = current_api.actuals_folder
	expected = current_api.api_expected
	data_org = current_api.data
	output_mode = current_api.output_mode
	status_code = current_api.status_code

	if output_mode != 'n':
		if output_mode == 'h':
			output_mode = 'a'
		f = codecs.open(filename + ".csv", output_mode,encoding='utf-16')
	else:
		f = None
	
	data_dict = json.loads (data_org)

	rowCount = 0

	result = check_status_code (status_code, expected["should_fail"])
	
	if status_code == 200:
		if not expected["specific"]:
			WriteHomeSlugHeader (f, output_mode)
			result, rowCount = WriteHomeSlug (f, data_dict, current_api)
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result