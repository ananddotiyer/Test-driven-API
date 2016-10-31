#!/usr/bin/env python

#############################################################################################################################################
"""export_social.py: Exports social api responses to csv."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from export_misc import *
from export_userdata import *

from ..libraries.verification import *

def WriteUploadContacts (f, rowCount, data_dict, current_api):
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

		for contact in data_dict["contacts"]:
			write (f, contact["phone"])
			write (f, contact["e164"])
			write (f, contact["parseStatus"])
			f.write ("\n")

			global_store (api_store, api_params, contact)
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteIPContacts (f, rowCount, data_dict, current_api):
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

		for contact in data_dict["list"]:
			write (f, contact["userId"])
			write (f, contact["displayName"])
			write (f, contact["image"])
			write (f, contact["thumbnail"])
			write (f, contact["status"])
			write (f, contact["blocked"])
			f.write ("\n")

			result = result and VerifyExpected (contact, expected)

		global_store (api_store, api_params, data_dict) #pagination
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteFollowers (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["list"], expected):
			return True

		for follower in data_dict["list"]:
			write (f, follower["following"])
			write (f, follower["userId"])
			write (f, follower["displayName"])
			write (f, follower["thumbnail"])
			write (f, follower["status"])
			write (f, follower["image"])
			write (f, follower["blurb"])
			write (f, data_dict["paginationParameter"])
		
			f.write ("\n")
			result = result and VerifyExpected (follower, expected)

		try:
			global_store (api_store, api_params, data_dict)
		except:
			pass

		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteFollowing (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["list"], expected):
			return True
		
		for following in data_dict["list"]:
			write (f, following["following"])
			write (f, following["userId"])
			write (f, following["displayName"])
			write (f, following["thumbnail"])
			write (f, following["status"])
			write (f, following["image"])
			write (f, following["blurb"])
			write (f, data_dict["paginationParameter"])
		
			f.write ("\n")
			result = result and VerifyExpected (following, expected)

		try:
			global_store (api_store, api_params, data_dict)
		except:
			pass

		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteSearchUsers (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["users"], expected):
			return True
		
		for user in data_dict["users"]:
			write (f, user["userId"])
			write (f, user["displayName"])
			write (f, user["nFollowing"])
			write (f, user["nFollowers"])
			write (f, user["thumbnail"])
			write (f, user["image"])
			write (f, user["status"])
			write (f, user["blurb"])
			write (f, user["nPosts"])
			write (f, data_dict["paginationParameter"])
		
			f.write ("\n")
			result = result and VerifyExpected (user, expected, False) #case in-sensitive

			try:
				global_store (api_store, api_params, data_dict) #pagination
			except:
				pass
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteUploadContactsHeader(f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("phone" + ","),
    f.write ("e164" + ","),
    f.write ("parseStatus" + "\n")

def WriteIPContactsHeader(f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("userId" + ","),
    f.write ("displayName" + ","),
    f.write ("image" + ","),
    f.write ("thumbnail" + ","),
    f.write ("status" + ","),
    f.write ("blocked" + "\n")

def WriteFollowersHeader(f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("following" + ","),
    f.write ("userId" + ","),
    f.write ("displayName" + ","),
    f.write ("thumbnail" + ","),
    f.write ("status" + ","),
    f.write ("image" + ","),
    f.write ("blurb" + ","),
    f.write ("paginationParameter" + "\n")

def WriteFollowingHeader(f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("following" + ","),
    f.write ("userId" + ","),
    f.write ("displayName" + ","),
    f.write ("thumbnail" + ","),
    f.write ("status" + ","),
    f.write ("image" + ","),
    f.write ("blurb" + ","),
    f.write ("paginationParameter" + "\n")

def WriteSearchUsersHeader(f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("userId" + ","),
    f.write ("displayName" + ","),
    f.write ("nFollowing" + ","),
    f.write ("nFollowers" + ","),
    f.write ("thumbnail" + ","),
    f.write ("image" + ","),
    f.write ("status" + ","),
    f.write ("blurb" + ","),
    f.write ("nPosts" + ","),
    f.write ("paginationParameter" + "\n")