#!/usr/bin/env python

#############################################################################################################################################
"""export_user.py: Exports user api responses to csv."""

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

def WriteAccessToken (f, rowCount, AccessToken, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (AccessToken, expected):
			return True

		write (f, AccessToken["userId"])
		write (f, AccessToken["accessToken"])
	
		f.write ("\n")

		global_store (api_store, api_params, AccessToken)
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteCognitoToken (f, rowCount, CognitoToken, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (CognitoToken, expected):
			return True

		write (f, CognitoToken["IdentityId"])
		write (f, CognitoToken["Token"])
	
		f.write ("\n")

		global_store (api_store, api_params, CognitoToken)
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteViewProfile (f, rowCount, ViewProfile, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (ViewProfile, expected):
			return True

		write (f, ViewProfile["displayName"])
		write (f, ViewProfile["blurb"])
		write (f, ViewProfile["status"])
		write (f, ViewProfile["thumbnail"])
		write (f, ViewProfile["image"])
		write (f, ViewProfile["nFollowers"])
		write (f, ViewProfile["nFollowing"])
		write (f, ViewProfile["vwBirthday"])
		write (f, ViewProfile["nPosts"])
	
		f.write ("\n")

		global_store (api_store, api_params, ViewProfile)
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteNotifications (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		FollowHeader = False
		CommentHeader = False
		SpinHeader = False
		LikeHeader = False
		
		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["notifications"], expected):
			return True
		
		headers = []
		
		for notification in sorted(data_dict["notifications"], key=lambda k: (k['notificationType'],k['timestamp'])):
			headers, userDisplayData = getUserDisplayDataInNotifications (notification, data_dict, headers)
			if notification["notificationType"] == 1: #Follow
				if not FollowHeader:
					FollowHeader = True
					WriteFollowHeader (f, output_mode, headers=headers)
				
				WriteNotificationFollow (f, notification, userDisplayData)
	
			if notification["notificationType"] == 2: #Comment
				if not CommentHeader:
					CommentHeader = True
					WriteCommentHeader (f, output_mode, headers=headers)

				WriteNotificationComment (f, notification, userDisplayData)
	
			if notification["notificationType"] == 3: #Spin
				if not SpinHeader:
					SpinHeader = True
					WriteSpinHeader (f, output_mode, headers=headers)

				WriteNotificationSpin (f, notification, userDisplayData)

			if notification["notificationType"] == 4: #Like
				if not LikeHeader:
					LikeHeader = True
					WriteLikeHeader (f, output_mode, headers=headers)

				WriteNotificationLike (f, notification, userDisplayData)
		
			f.write ("\n")
			result = result and VerifyExpected (notification, expected)

			try:
				global_store (api_store, api_params, notification)
			except:
				pass
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteLoop (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		TextHeader = False
		ShareHeader = False
		ImageHeader = False
		voxPicHeader = False
		imageTextHeader = False
		
		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["posts"], expected):
			return True
		
		headers = []
		
		for post in sorted(data_dict["posts"], key=lambda k: k['postType']):
			headers, userDisplayData = getUserDisplayDataInPosts (post, data_dict, headers)
			if post["postType"] == 1: #Text
				if not TextHeader:
					TextHeader = True
					WriteTextHeader (f, output_mode, headers=headers)

				WritePostText (f, post, userDisplayData=userDisplayData)

			if post["postType"] == 3: #share
				if not ShareHeader:
					ShareHeader = True
					WriteShareHeader (f, output_mode, headers=headers)

				WritePostShare (f, post, userDisplayData=userDisplayData)

			if post["postType"] == 4: #image
				if not ImageHeader:
					ImageHeader = True
					WriteImageHeader (f, output_mode, headers=headers)

				WritePostImage (f, post, userDisplayData=userDisplayData)
	
			if post["postType"] == 5: #voxPic
				if not voxPicHeader:
					voxPicHeader = True
					WritevoxPicHeader (f, output_mode, headers=headers)

				WritePostvoxPic (f, post, userDisplayData=userDisplayData)

			if post["postType"] == 9: #imageText
				if not imageTextHeader:
					imageTextHeader = True
					WriteimageTextHeader (f, output_mode, headers=headers)

				WritePostimageText (f, post, userDisplayData=userDisplayData)
		
			f.write ("\n")
			
			result = result and VerifyExpected (post, expected)

			try:
				global_store (api_store, api_params, post)
			except:
				pass
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteAccessTokenHeader (f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("userId" + ","),
    f.write ("accessToken" + "\n"),

def WriteViewProfileHeader (f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("displayName" + ","),
    f.write ("blurb" + ","),
    f.write ("status" + ","),
    f.write ("thumbnail" + ","),
    f.write ("image" + ","),
    f.write ("nFollowers" + ","),
    f.write ("nFollowing" + ","),
    f.write ("vwBirthday" + ","),
    f.write ("nPosts" + "\n")