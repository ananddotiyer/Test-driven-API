#!/usr/bin/env python

#############################################################################################################################################
"""api_functions.py: Parsing api responses, verification of responses against expected output."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer", "Aarthy S", "Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from ..export.export_user import *
from ..export.export_social import *
from ..export.export_life import *
from ..export.export_misc import *
from verification import *
from ..tests.tests_suite import *
from base64 import b64encode
import json
import codecs

################################################user##############################################################
def getVerificationCode(current_api):
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
	
	if not expected["specific"]:
		rowCount += 1
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getAccessToken(current_api):
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
			rowCount += 1
			userAndPass = str (b64encode (data_dict["userId"] + ":" + data_dict["accessToken"]).decode("ascii"))
			global_dict["headers"]["Authorization"] = "Basic %s" %  userAndPass
			WriteAccessTokenHeader (f, output_mode)
			result = WriteAccessToken (f, rowCount, data_dict, current_api)
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getCognitoToken(current_api):
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
			rowCount += 1
			WriteCognitoTokenHeader (f, output_mode)
			result = WriteCognitoToken (f, rowCount, data_dict, current_api)
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def updateProfile(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)
		
	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def viewProfile(current_api):
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
			rowCount += 1
			WriteViewProfileHeader (f, output_mode)
			result = WriteViewProfile (f, rowCount, data_dict["userSummary"], current_api)
			result = result and VerifyExpected (data_dict["userSummary"], expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getNotifications(current_api):
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

	result = check_status_code (status_code, expected["should_fail"])
	
	if status_code == 200:
		if not expected["specific"]:
			rowCount = len (data_dict["notifications"])
			result = WriteNotifications (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getLoop (current_api):
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

	result = check_status_code (status_code, expected["should_fail"])
	
	if status_code == 200:
		if not expected["specific"]:
			rowCount = len (data_dict["posts"])
			result = WriteLoop (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

################################################social##############################################################
def uploadContacts(current_api):
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
			rowCount = len (data_dict["contacts"])
			WriteUploadContactsHeader (f, output_mode)
			result = WriteUploadContacts (f, rowCount, data_dict, current_api)
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getIPContacts(current_api):
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
			rowCount = len (data_dict["list"])
			WriteIPContactsHeader (f, output_mode)
			result = WriteIPContacts (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def blockContact(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def unblockContact(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def followUser(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def unfollowUser(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getFollowers(current_api):
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
			rowCount = len (data_dict["list"])
			WriteFollowersHeader (f, output_mode)
			result = WriteFollowers (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getFollowing(current_api):
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
			rowCount = len (data_dict["list"])
			WriteFollowingHeader (f, output_mode)
			result = WriteFollowing (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def searchUser(current_api):
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
			rowCount = len (data_dict["users"])
			WriteSearchUsersHeader (f, output_mode)
			result = WriteSearchUsers (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

################################################life##############################################################
def getLifePage (current_api):
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

	result = check_status_code (status_code, expected["should_fail"])
	
	if status_code == 200:
		if not expected["specific"]:
			rowCount = len (data_dict["posts"])
			result = WriteLifePage (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def uploadLifePost(current_api):
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
			rowCount += 1
			result = WriteUploadPost (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)
		

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getLifePost (current_api):
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
			try:
				data_dict["postObject"]
				rowCount = 1 #either 1 post
			except:
				rowCount = len (data_dict["posts"]) #or multiple posts
			
			result = WriteLifePost (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def removeVoiceFromVoxPic(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def deleteLifePost(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def uploadLike(current_api):
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
			rowCount += 1
			result = WriteUploadLike (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def deleteLike(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getPostLikes(current_api):
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
			WritePostLikeHeader (f, output_mode)
			for like in data_dict["likes"]:
				rowCount += 1
				result = WritePostLike (f, rowCount, like, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def uploadComment(current_api):
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
			rowCount += 1
			result = WriteComment (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)


	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getPostComments(current_api):
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
			rowCount = len (data_dict["comments"])
			result = WriteComment (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def getHashtagPage (current_api):
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
			result, rowCount = WriteHashtagPage (f, rowCount, data_dict, current_api)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result

def reportContent(current_api):
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
			rowCount += 1
			result = result and VerifyExpected (data_dict, expected)
	else:
		result = result and VerifyExpected (data_dict, expected)

	result = result and VerifyRowCount (rowCount, expected["rowcount"])
			
	try:
		f.close()
	except:
		pass

	return result
