#!/usr/bin/env python

#############################################################################################################################################
"""export_life.py: Exports life api responses to csv."""

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

def WriteLifePage (f, rowCount, data_dict, current_api):
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

		try:
			following = data_dict["following"]
			headers.append ("following")
		except:
			following = None

		try:
			lifeSummary = data_dict["lifeSummary"]
			headers.append ("lifeSummary")
		except:
			lifeSummary = None
		
		for post in sorted(data_dict["posts"], key=lambda k: k['postType']):
			headers, userDisplayData = getUserDisplayDataInPosts (post, data_dict, headers)
			if post["postType"] == 1: #Text
				if not TextHeader:
					TextHeader = True
					WriteTextHeader (f, output_mode, headers=headers)

				WritePostText (f, post, userDisplayData=userDisplayData, following=following, lifeSummary=lifeSummary)

			if post["postType"] == 3: #share
				if not ShareHeader:
					ShareHeader = True
					WriteShareHeader (f, output_mode, headers=headers)

				WritePostShare (f, post, userDisplayData=userDisplayData, following=following, lifeSummary=lifeSummary)

			if post["postType"] == 4: #image
				if not ImageHeader:
					ImageHeader = True
					WriteImageHeader (f, output_mode, headers=headers)

				WritePostImage (f, post, userDisplayData=userDisplayData, following=following, lifeSummary=lifeSummary)
	
			if post["postType"] == 5: #voxPic
				if not voxPicHeader:
					voxPicHeader = True
					WritevoxPicHeader (f, output_mode, headers=headers)

				WritePostvoxPic (f, post, userDisplayData=userDisplayData, following=following, lifeSummary=lifeSummary)

			if post["postType"] == 9: #imageText
				if not imageTextHeader:
					imageTextHeader = True
					WriteimageTextHeader (f, output_mode, headers=headers)

				WritePostimageText (f, post, userDisplayData=userDisplayData, following=following, lifeSummary=lifeSummary)
		
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

def WriteUploadPost (f, rowCount, data_dict, current_api):
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

		post = data_dict["postObject"]
		
		if not VerifyFilter (post, expected):
			return True
		
		if post["postType"] == 1: #Text
			if not TextHeader:
				TextHeader = True
				WriteTextHeader (f, output_mode, upload=True)

			WritePostText (f, post, upload=True)

		if post["postType"] == 3: #share
			if not ShareHeader:
				ShareHeader = True
				WriteShareHeader (f, output_mode, upload=True)

			WritePostShare (f, post, upload=True)

		if post["postType"] == 4: #image
			if not ImageHeader:
				ImageHeader = True
				WriteImageHeader (f, output_mode, upload=True)

			WritePostImage (f, post, upload=True)

		if post["postType"] == 5: #voxPic
			if not voxPicHeader:
				voxPicHeader = True
				WritevoxPicHeader (f, output_mode, upload=True)

			WritePostvoxPic (f, post, upload=True)

		if post["postType"] == 9: #imageText
			if not imageTextHeader:
				imageTextHeader = True
				WriteimageTextHeader (f, output_mode, upload=True)

			WritePostimageText (f, post, upload=True)
		
		f.write ("\n")
			
		result = result and VerifyExpected (data_dict, expected)

		try:
			global_store (api_store, api_params, post)
		except:
			pass
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteLifePost (f, rowCount, data_dict, current_api):
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
		post_list = []
		
		if (output_mode == 'n'):
			return True		

		try:
			post_list.append (data_dict["postObject"]) #single post
		except:
			post_list.extend (data_dict["posts"]) #multiple posts
			
		if not VerifyFilter (post_list, expected):
			return True
			
		headers = []

		for post in sorted(post_list, key=lambda k: k['postType']):
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

def WriteUploadLike (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		like = data_dict["likeObject"]
		
		if not VerifyFilter (like, expected):
			return True
		
		if like != "null":
			WriteUploadLikeHeader (f, output_mode)
			write (f, like["postId"])
			write (f, like["userId"])
			write (f, like["timestamp"])
			write (f, like["likeId"])
			write (f, like["_id"])	
		
		f.write ("\n")
		
		result = result and VerifyExpected (data_dict, expected)

		try:
			global_store (api_store, api_params, like)
		except:
			pass
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WritePostLike (f, rowCount, like, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (like, expected):
			return True
		
		write (f, like["timestamp"])
		write (f, like["userId"])
		write (f, like["likeId"])
		write (f, like["displayName"])
		write (f, like["thumbnail"])	
		write (f, like["image"])	
		
		f.write ("\n")
		
		result = result and VerifyExpected (like, expected)

		try:
			global_store (api_store, api_params, like)
		except:
			pass
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteComment (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		CommentDataHeader = False
		
		result = True
		comment_list = []
		
		if (output_mode == 'n'):
			return True		

		try:
			comment_list.append (data_dict["commentObject"]) #single comment
		except:
			comment_list.extend (data_dict["comments"]) #multiple comments

		if not VerifyFilter (comment_list, expected):
			return True

		headers = []
		
		for comment in comment_list:
			headers, userDisplayData = getUserDisplayDataInComments (comment, data_dict, headers)
			if not CommentDataHeader:
				CommentDataHeader = True
				WriteCommentDataHeader (f, output_mode, headers=headers)
			WriteCommentData (f, comment, userDisplayData=userDisplayData)
			
			f.write ("\n")
		
			result = result and VerifyExpected (data_dict, expected)
	
			try:
				global_store (api_store, api_params, comment)
			except:
				pass
		
		return result
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteHashtagPage (f, rowCount, data_dict, current_api):
	try:
		expected = current_api.api_expected
		api_store = current_api.api_store
		api_params = current_api.api_params
		output_mode = current_api.output_mode

		CommentDataHeader = False
		PostDataHeader = False
		
		result = True
		
		if (output_mode == 'n'):
			return True		

		if not VerifyFilter (data_dict["list"], expected):
			return True
		
		headers = []

		for item in sorted(data_dict["list"], key=lambda k: k['type']):
			rowCount += 1
			if item["type"] == "comment": #Comment item
				headers, userDisplayData = getUserDisplayDataInPosts (item, data_dict, headers)
				if not CommentDataHeader:
					CommentDataHeader = True
					WriteCommentDataHeader (f, output_mode, headers=headers)

				WriteCommentData (f, item["content"], userDisplayData=userDisplayData)

			if item["type"] == "post": #Post item
				headers, userDisplayData = getUserDisplayDataInComments (item, data_dict, headers)
				if not PostDataHeader:
					PostDataHeader = True
					WritePostDataHeader (f, output_mode, headers=headers)

				WritePostData (f, item["content"], userDisplayData=userDisplayData)

			f.write ("\n")
			
			result = result and VerifyExpected (item, expected)

			try:
				global_store (api_store, api_params, item)
			except:
				pass
		return result, rowCount
	except Exception, e:
		report_it ("Row " + str (rowCount + 1) + ":" + str(e) + " field is missing in the server response (JSON)\n")
		f.write ("\n")
		return False

def WriteUploadLikeHeader (f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("postId" + ","),
    f.write ("userId" + ","),
    f.write ("timestamp" + ","),
    f.write ("likeId" + ","),
    f.write ("_id" + "\n")

def WritePostLikeHeader (f, output_mode):
    if (output_mode != 'w') and (output_mode != 'h'):
        return
    f.write ("timestamp" + ","),
    f.write ("userId" + ","),
    f.write ("likeId" + ","),
    f.write ("displayName" + ","),
    f.write ("thumbnail" + ","),
    f.write ("image" + "\n")