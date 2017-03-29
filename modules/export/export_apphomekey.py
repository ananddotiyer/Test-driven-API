#!/usr/bin/env python

#############################################################################################################################################
"""export_apphomekey.py: Exports apphomekey api responses to csv."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Moolya Software Testing"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "anand.iyer@moolya.com"
__status__ = "Production"
#############################################################################################################################################

from export_misc import *

from ..libraries.verification import *

def WriteHomeSlug (f, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict, expected):
			return True

		rowCount = 0
		for item in data_dict["item"]:
			rowCount += 1
			WriteItemDetails (f, item)
			
			try:
				global_store (api_store, api_params, item)
			except:
				pass
		return result, rowCount
	except Exception, e:
		report_it ("Row " + str (rowCount) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteItemDetails (f, item):
	write (f, item["id"])
	#write (f, item["name"])
	write (f, item["typeId"])
	write (f, item["type"])
	#write (f, item["video_id"])
	f.write ("\n")
	
def WriteHomeSlugHeader (f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("id" + ","),
    #f.write ("name" + ","),
    f.write ("typeId" + ","),
    f.write ("type" + ","),
    f.write ("video_id" + "\n")