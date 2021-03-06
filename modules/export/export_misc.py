#!/usr/bin/env python

#############################################################################################################################################
"""export_misc.py: Some common support functions for exporting api responses to csv."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################
import traceback
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

def global_store (api_store, api_params, data, global_dict):
	#storing into global_dict

	try:
		old_data = data #store, in order to restore later
		for each in api_store["response"].keys ():
			var = api_store["response"][each]
			data = old_data #before next iteration starts
			try:
				if each != "":
					jsonpath_expr = parse(each)
					store_data = [match.value for match in jsonpath_expr.find(data)]
					#above match gives a list with an embedded list, containing all items;
					#this means, we need to get the first item in the list, before we can access its contents
					if len (store_data) == 1:
						store_data = store_data[0]
				else:
					store_data = []
					store_data.append (data)
			except:
				pass 
			try:
				global_dict[var] = store_data
			except:
				print ("Unable to find " + each + " in the server response!  None stored.")

		old_data = api_params #store, in order to restore later
		for each in api_store["request"].keys():
			var = api_store["request"][each]
			data = old_data #before next iteration starts
			try:
				if each != "":
					jsonpath_expr = parse(each)
					store_data = [match.value for match in jsonpath_expr.find(data)]
					#above match gives a list with an embedded list, containing all items;
					#this means, we need to get the first item in the list, before we can access its contents
					if len (store_data) == 1:
						store_data = store_data[0]
				else:
					store_data = []
					store_data.append (data)
			except:
				pass 
			try:
				global_dict[var] = store_data
			except:
				print ("Unable to find " + each + " in the request parameters!  None stored.")

	except:
		pass

####Generic####
def WriteRow (f, data_dict, current_api, global_dict):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		try:
			global_store (api_store, api_params, data_dict, global_dict)
		except:
			pass

		if (output_mode == 'n'):
			return
		if type (data_dict) == list:
			WriteHeader (f, data_dict[0].keys(), output_mode) #get header from the first row of data_dict
			for row in data_dict:
				WriteRowDetails (f, row)
		else:
			WriteHeader (f, data_dict.keys(), output_mode)
			WriteRowDetails (f, data_dict)

	except Exception, e:
		traceback.print_exc ()
		#report_it ("Row " + str (rowCount) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		#f.write ("\n")
		
def WriteRowDetails (f, row):
	row_string = ""
	for column in row.values ():
		row_string += "%s\t" %(unicode (column))

	row_string = row_string.replace ('\n', '').strip (',')
	f.write (row_string + "\n")
	
def WriteHeader (f, headers, output_mode):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	header_string = ""
	for header in headers:
		header_string += "%s\t" %(unicode (header))

	header_string = header_string.strip (',')
	f.write (header_string + "\n")