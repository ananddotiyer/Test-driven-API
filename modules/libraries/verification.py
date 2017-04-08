#!/usr/bin/env python

#############################################################################################################################################
"""verification.py: Verifies api responses, creates filters for csv export, and reports"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

import json
import datetime
import re
import sys
import traceback
import json_schema
from modules.tests.tests_suite import *
from jsonpath_rw import jsonpath, parse

def compare_equals (json_path, actual, expected):
    jsonpath_expr = parse(json_path)
    actual = [match.value for match in jsonpath_expr.find(actual)]
    if not (set (actual) == set (expected)): #contains or equal
        error_message = "Expected %s in %s, but found %s" %(str (expected), json_path, str (actual))
        print error_message
        global_dict["debuglog"].write (error_message + "\n")
        return False
    else:
        return True

def compare_contains (json_path, actual, expected):
    jsonpath_expr = parse(json_path)
    actual = [match.value for match in jsonpath_expr.find(actual)]
    if not (set (actual) <= set (expected)): #contains or equal
        error_message = "Expected %s in %s, but found %s" %(str (expected), json_path, str (actual))
        print error_message
        global_dict["debuglog"].write (error_message + "\n")
        return False
    else:
        return True

def compare_types (json_path, actual, expected):
    jsonpath_expr = parse(json_path)
    actual = [match.value for match in jsonpath_expr.find(actual)]
    if not (type (actual[0]) == expected): #same type
        error_message = "Expected %s in %s, but found %s" %(expected, json_path, type (actual[0]))
        print error_message
        global_dict["debuglog"].write (error_message + "\n")
        return False
    else:
        return True

def get_response_schema (response, write_file):
	try:
		schema = json_schema.dumps(response)
		with open (write_file, "w") as s:
			s.write (schema)
	except:
		traceback.print_exc(file=sys.stdout)

def create_schema (schema):
	try:
		schema_contents =""
		with open (schema) as s:
			for line in s:
				schema_contents += line

		#schema_object = json_schema.loads(schema_contents)
		return schema_contents
	except:
		traceback.print_exc(file=sys.stdout)
	
def full_match_schema (data, schema_object):
	try:
		return schema_object.full_check (data)
	except:
		traceback.print_exc(file=sys.stdout)

def match_schema (data, schema_object):
	try:
		return json_schema.match (data, schema_object)
	except:
		traceback.print_exc(file=sys.stdout)

def VerifyFilter (actual, expected):
    retValue = True
    try:
        for each in expected["filter"]["location"].split ('\\'):
            actual = actual[each]
    except:
        pass #No location is specified.  So, filter from the base location.
    
    try:
        for each in expected["filter"]:
            global_dict["debuglog"].write ("Actual: " + str (actual[each]) + ", Expected: " + expected["filter"][each] + "\n")
            if (isinstance (actual[each], list)):
                if not (expected["filter"][each] in (actual[each])):
                    global_dict["debuglog"].write ("Values don't match\n")
                    retValue = False
                    break
            elif not (isinstance (actual[each], dict)):
                if not (str (actual[each]) == expected["filter"][each]):
                    retValue = False
                    break
    except:
        pass #filter dictionary might not be available in the test
    return retValue

def VerifyRowCount (actual_rowCount, exp_rowCount):
    if not (exp_rowCount == actual_rowCount):
        print (str (exp_rowCount) + " rows expected, but " + str (actual_rowCount) + "found!")
        global_dict["debuglog"].write (str (exp_rowCount) + " rows expected, but " + str (actual_rowCount) + "found!\n")
        return False
    else:
        return True

def VerifyExpected (actual, expected, json_file=None, case_sensitive=True):
    result = True
    actual_flattened = ""

    #match json structure exported from api_functions
    try:
        response_schema = expected["response_schema"]
    except:
        response_schema = "none"
        
    if response_schema == "match":
        schema = create_schema (json_file)
        if not match_schema (actual, schema):
            result = False
            schema_object = json_schema.loads(schema)
            full_match_output = full_match_schema (actual, schema_object)
            print "Schema of resultant JSON response not matching with expected schema.  Check debuglog for details."
            global_dict["debuglog"].write (full_match_output + "\n")
        else:
            result = True
            print "Schema match successful"
            
    actual = json.loads (actual)

    old_actual = actual #store, in order to restore later
    try:
        for exp in expected.keys():
            actual = old_actual #before next iteration starts
            
            if (exp == "rowcount") or (exp == "specific") or (exp == "filter") or (exp == "should_fail"):
                continue
            
            try:
                if exp[:5] == "call_":
                    function = getattr (sys.modules[__name__], exp[5:])
                    for json_path in expected[exp].keys():
                        result = result and function (json_path, actual, expected[exp][json_path])
            except:
                pass
    except:
        result = False
        
    return result

def check_status_code (status_code, should_fail):
	if status_code != 200:
		if not should_fail:
			result = False
		else:
			result = True
	else:
		if not should_fail:
			result = True
		else:
			result = False
	
	return result

def report_start ():
    #global_dict["reslog"].write ("test_path,api_url,api_type,executed_at,time_spent (sec),result\n")
    global_dict["start_time"] = datetime.datetime.now()
    
def report_it (result, test="", api_url="", api_type=""):
    #print (result)
    if isinstance (result, bool):
        if (result):
            print ("All is well!!")
            global_dict["debuglog"].write ("All is well!!\n")
            global_dict["reslog"].write ("PASS\n")
        else:
            global_dict["reslog"].write ("FAIL\n")
    else:
        result = str (result)
        global_dict["stop_time"] = datetime.datetime.now()
        date_time = global_dict["stop_time"].strftime('%Y-%m-%d %H:%M:%S')
        time_spent = str ((global_dict["stop_time"] - global_dict["start_time"]).total_seconds())
        result_string = test + " (Executed: " + date_time + ", " + time_spent + " seconds)"
        global_dict["start_time"] = global_dict["stop_time"]
        
        if result == "datetime":
            global_dict["debuglog"].write ("\n**" + result_string + "**\n") #only if this is the test header
            print "\n"
            print ("**************************************************************************************")
            print (result_string)
            print ("**************************************************************************************")
            
            #Hyper-link the test to the appropriate output .csv.  For the right hyperlinking technique, refer to http://stackoverflow.com/questions/6563091/can-excel-interpret-the-urls-in-my-csv-as-hyperlinks
            test_title = test
            test = re.sub (r"^\\(.+)\\.*\\(.+)$", r"\1\\actuals\\\2", test) #lazy match ensures that only the test name is replaced.
            global_dict["reslog"].write ("\"=HYPERLINK(\"\"" + test + ".csv\"\"" + "," + "\"\"" + test + "\"\")\"" + "," +
                                         api_url + "," + api_type + "," + date_time + "," + time_spent + ",")
        else:
            global_dict["debuglog"].write (result)
            print (result)
            
