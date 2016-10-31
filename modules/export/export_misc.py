#!/usr/bin/env python

#############################################################################################################################################
"""export_misc.py: Some common support functions for exporting api responses to csv."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from ..libraries.verification import *

def write_none(f, val):
	if val is None:
		f.write (","),
	else:
		if isinstance (val, int):
			f.write (str (val) + ","),
		else:
			f.write (val + ",")
	

def write (f, column, embed=False, ends_with=','):
    if column is None:
        f.write (","),
    else:
        if isinstance (column, list):
            all_each = ""
            for each in column:
                all_each += each + ".." #;
            column = all_each #concatenate everything into a string
        elif isinstance  (column, int) or isinstance  (column, long):
            column = str (column)

        #if '\"' in column:
        #    embed = True

        embed = True        
        if embed:
            f.write ("\"")

        f.write (column.replace ("\"", "'").replace (",", "|").encode('utf-8')), #+

        if embed:
            f.write ("\"")

        f.write (ends_with)

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

def global_store (api_store, api_params, data):
	#storing into global_dict
	try:
		for each in api_store["response"]:
			try:
				for each in api_store["response"].keys()[0].split ('\\'):
					data = data[each]
			except:
				pass #No location is specified.  So, base location.    
			try:
				#global_dict[each] = data[api_store["response"][each]]
				global_dict[each] = data
				print (global_dict[each])
			except:
				print ("Unable to find " + each + " in the server response!  None stored.")

		for each in api_store["request"]:
			try:
				for each in api_store["response"].keys()[0].split ('\\'):
					data = data[each]
			except:
				pass #No location is specified.  So, base location.    
			try:
				#global_dict[each] = api_params[api_store["request"][each]]
				global_dict[each] = api_params
				print (global_dict[each])
			except:
				print ("Unable to find " + each + " in the request parameters!  None stored.")

	except:
		pass