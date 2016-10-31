#!/usr/bin/env python

#############################################################################################################################################
"""export_userdata.py: Support functions for exporting api responses to csv."""

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
from json import *

def WriteHashTagStr (f, data_dict):
	strhashtag = ""
	for hashtag in data_dict["hashtags"]:
		strhashtag += hashtag

	write (f, strhashtag)

def WriteCommentStr (f, data_dict):
	strcomment = ""
	for comment in data_dict["comments"]:
		strcomment += json.dumps (comment)

	write (f, strcomment)

def WriteUserDisplayData (f, userDisplayData):
	#write (f, userDisplayData["displayName"])
	#write (f, userDisplayData["thumbnail"])
	#write (f, userDisplayData["image"])
	write (f, json.dumps (userDisplayData))

def Writefollowing (f, following):
	write (f, following["following"])
	#write (f, following["timestamp"])

def WritelifeSummary (f, lifeSummary):
	write (f, lifeSummary["userId"])
	write (f, lifeSummary["displayName"])
	write (f, lifeSummary["status"])
	write (f, lifeSummary["blurb"])
	write (f, lifeSummary["thumbnail"])
	write (f, lifeSummary["image"])
	write (f, lifeSummary["nFollowers"])
	write (f, lifeSummary["vwBirthday"])
	write (f, lifeSummary["nPosts"])
	write (f, lifeSummary["nFollowing"])

def WriteNotificationFollow (f, notification, userDisplayData):
	write (f, notification["notificationId"])
	write (f, notification["notificationType"])
	write (f, notification["userId"])
	write (f, notification["followUserId"])
	write (f, notification["timestamp"])
	WriteUserDisplayData (f, userDisplayData)

def WriteNotificationComment (f, notification, userDisplayData):
	write (f, notification["notificationId"])
	write (f, notification["notificationType"])
	write (f, notification["userId"])
	write (f, notification["commentUserId"])
	write (f, notification["timestamp"])
	write (f, notification["commentId"])
	write (f, notification["postId"])
	WriteUserDisplayData (f, userDisplayData)

def WriteNotificationSpin (f, notification, userDisplayData):
	write (f, notification["notificationId"])
	write (f, notification["notificationType"])
	write (f, notification["spinPostId"])
	write (f, notification["spinUserId"])
	write (f, notification["derivativePostParent"])
	write (f, notification["timestamp"])
	write (f, notification["userId"])
	WriteUserDisplayData (f, userDisplayData)

def WriteNotificationLike (f, notification, userDisplayData):
	write (f, notification["notificationId"])
	write (f, notification["notificationType"])
	write (f, notification["userId"])
	write (f, notification["likeUserId"])
	write (f, notification["timestamp"])
	write (f, notification["likeId"])
	write (f, notification["postId"])
	WriteUserDisplayData (f, userDisplayData)

def WritePostText (f, post, upload=False, userDisplayData=None, following=None, lifeSummary=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["postText"])

	if not upload:
		WriteCommentStr (f, post)
		write (f, post["isLiked"]["isLiked"])
	
	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

	if following != None:
		Writefollowing (f, following)

	if lifeSummary != None:
		WritelifeSummary (f, lifeSummary)

def WritePostShare (f, post, upload=False, userDisplayData=None, following=None, lifeSummary=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["originalPostId"])

	if not upload:
		WriteCommentStr (f, post)
		write (f, post["isLiked"]["isLiked"])
	
	#originalpostcontent
	originalPostContent = ""
	try:
		originalPostContent = post["originalPostContent"] #only for getLifePage
	except:
		pass
	
	#write (f, originalPostContent["userId"])
	#write (f, originalPostContent["postType"])
	#write (f, originalPostContent["nComments"])
	#write (f, originalPostContent["nLikes"])
	#write (f, originalPostContent["timestamp"])
	#WriteHashTagStr (f, originalPostContent)
	#write (f, originalPostContent["postId"])
	#write (f, originalPostContent["postImage"])
	#write (f, originalPostContent["postAudio"])
	#write (f, originalPostContent["isLiked"]["isLiked"])
	#WriteCommentStr (f, originalPostContent)
	write (f, json.dumps (originalPostContent))
	
	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

	if following != None:
		Writefollowing (f, following)

	if lifeSummary != None:
		WritelifeSummary (f, lifeSummary)

def WritePostImage (f, post, upload=False, userDisplayData=None, following=None, lifeSummary=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["postImage"])

	if not upload:
		WriteCommentStr (f, post)
		write (f, post["isLiked"]["isLiked"])

	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

	if following != None:
		Writefollowing (f, following)

	if lifeSummary != None:
		WritelifeSummary (f, lifeSummary)

def WritePostvoxPic (f, post, upload=False, userDisplayData=None, following=None, lifeSummary=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["postImage"])
	write (f, post["postAudio"])

	if not upload:
		WriteCommentStr (f, post)
		write (f, post["isLiked"]["isLiked"])

	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

	if following != None:
		Writefollowing (f, following)

	if lifeSummary != None:
		WritelifeSummary (f, lifeSummary)

def WritePostimageText (f, post, upload=False, userDisplayData=None, following=None, lifeSummary=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["postImage"])
	write (f, post["postText"])

	if not upload:
		WriteCommentStr (f, post)
		write (f, post["isLiked"]["isLiked"])

	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

	if following != None:
		Writefollowing (f, following)

	if lifeSummary != None:
		WritelifeSummary (f, lifeSummary)

def WriteCommentData (f, comment, userDisplayData=None):
	write (f, comment["postId"])
	write (f, comment["userId"])
	write (f, comment["commentText"])
	WriteHashTagStr (f, comment)
	write (f, comment["timestamp"])
	write (f, comment["commentId"])
	write (f, comment["_id"])

	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

def WritePostData (f, post, userDisplayData=None):
	write (f, post["userId"])
	write (f, post["postType"])
	write (f, post["nComments"])
	write (f, post["nLikes"])
	write (f, post["timestamp"])
	WriteHashTagStr (f, post)
	write (f, post["postId"])
	write (f, post["postText"])
	write (f, post["_id"])

	if userDisplayData != None:
		WriteUserDisplayData (f, userDisplayData)

def WriteFollowHeader (f, output_mode, headers=[]):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	f.write ("\n")
	f.write ("notificationId" + ","),
	f.write ("notificationType" + ","),
	f.write ("userId" + ","),
	f.write ("followUserId" + ","),
	f.write ("timestamp" + ","),
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")
	
def WriteCommentHeader (f, output_mode, headers=[]):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	f.write ("\n")
	f.write ("notificationId" + ","),
	f.write ("notificationType" + ","),
	f.write ("userId" + ","),
	f.write ("commentUserId" + ","),
	f.write ("timestamp" + ","),
	f.write ("commentId" + ","),
	f.write ("postId" + ","),
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")

def WriteSpinHeader (f, output_mode, headers=[]):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	f.write ("\n")
	f.write ("notificationId" + ","),
	f.write ("notificationType" + ","),
	f.write ("spinPostId" + ","),
	f.write ("spinUserId" + ","),
	f.write ("derivativePostParent" + ","),
	f.write ("timestamp" + ","),
	f.write ("userId" + ","),
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")

def WriteLikeHeader (f, output_mode, headers=[]):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	f.write ("\n")
	f.write ("notificationId" + ","),
	f.write ("notificationType" + ","),
	f.write ("userId" + ","),
	f.write ("likeUserId" + ","),
	f.write ("timestamp" + ","),
	f.write ("likeId" + ","),
	f.write ("postId" + ","),
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")

def WriteTextHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("postText" + ","),
	
	if not upload:
		f.write ("comments" + ","),
		f.write ("isLiked" + ","),
	
	if "userDisplayData" in headers:
		#f.write ("displayName" + ","),
		#f.write ("thumbnail" + ","),
		#f.write ("image" + ","),
		f.write ("userDisplayData" + ","),

	if "following" in headers:
		f.write ("following" + ","),
		#f.write ("timestamp" + ","),

	if "lifeSummary" in headers:
		f.write ("userId" + ","),
		f.write ("displayName" + ","),
		f.write ("status" + ","),
		f.write ("blurb" + ","),
		f.write ("thumbnail" + ","),
		f.write ("image" + ","),
		f.write ("nFollowers" + ","),
		f.write ("vwBirthday" + ","),
		f.write ("nPosts" + ","),
		f.write ("nFollowing" + ","),

	f.write ("\n")

def WriteShareHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("originalPostId" + ","),

	if not upload:
		f.write ("comments" + ","),
		f.write ("isLiked" + ","),

	#f.write ("orig_userId" + ","),
	#f.write ("orig_postType" + ","),
	#f.write ("orig_nComments" + ","),
	#f.write ("orig_nLikes" + ","),
	#f.write ("orig_timestamp" + ","),
	#f.write ("orig_hashtags" + ","),
	#f.write ("orig_postId" + ","),
	#f.write ("orig_postImage" + ","),
	#f.write ("orig_postAudio" + ","),
	#f.write ("orig_isLiked" + ","),
	#f.write ("orig_comments" + ","),
	f.write ("orig_post" + ","),

	if "userDisplayData" in headers:
		#f.write ("displayName" + ","),
		#f.write ("thumbnail" + ","),
		#f.write ("image" + ","),
		f.write ("userDisplayData" + ","),

	if "following" in headers:
		f.write ("following" + ","),
		#f.write ("timestamp" + ","),

	if "lifeSummary" in headers:
		f.write ("userId" + ","),
		f.write ("displayName" + ","),
		f.write ("status" + ","),
		f.write ("blurb" + ","),
		f.write ("thumbnail" + ","),
		f.write ("image" + ","),
		f.write ("nFollowers" + ","),
		f.write ("vwBirthday" + ","),
		f.write ("nPosts" + ","),
		f.write ("nFollowing" + ","),

	f.write ("\n")

def WriteImageHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("postImage" + ","),

	if not upload:
		f.write ("comments" + ","),
		f.write ("isLiked" + ","),

	if "userDisplayData" in headers:
		#f.write ("displayName" + ","),
		#f.write ("thumbnail" + ","),
		#f.write ("image" + ","),
		f.write ("userDisplayData" + ","),

	if "following" in headers:
		f.write ("following" + ","),
		#f.write ("timestamp" + ","),

	if "lifeSummary" in headers:
		f.write ("userId" + ","),
		f.write ("displayName" + ","),
		f.write ("status" + ","),
		f.write ("blurb" + ","),
		f.write ("thumbnail" + ","),
		f.write ("image" + ","),
		f.write ("nFollowers" + ","),
		f.write ("vwBirthday" + ","),
		f.write ("nPosts" + ","),
		f.write ("nFollowing" + ","),

	f.write ("\n")

def WritevoxPicHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return

	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("postImage" + ","),
	f.write ("postAudio" + ","),

	if not upload:
		f.write ("comments" + ","),
		f.write ("isLiked" + ","),

	if "userDisplayData" in headers:
		#f.write ("displayName" + ","),
		#f.write ("thumbnail" + ","),
		#f.write ("image" + ","),
		f.write ("userDisplayData" + ","),

	if "following" in headers:
		f.write ("following" + ","),
		#f.write ("timestamp" + ","),

	if "lifeSummary" in headers:
		f.write ("userId" + ","),
		f.write ("displayName" + ","),
		f.write ("status" + ","),
		f.write ("blurb" + ","),
		f.write ("thumbnail" + ","),
		f.write ("image" + ","),
		f.write ("nFollowers" + ","),
		f.write ("vwBirthday" + ","),
		f.write ("nPosts" + ","),
		f.write ("nFollowing" + ","),

	f.write ("\n")

def WriteimageTextHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return

	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("postImage" + ","),
	f.write ("postText" + ","),

	if not upload:
		f.write ("comments" + ","),
		f.write ("isLiked" + ","),

	if "userDisplayData" in headers:
		#f.write ("displayName" + ","),
		#f.write ("thumbnail" + ","),
		#f.write ("image" + ","),
		f.write ("userDisplayData" + ","),

	if "following" in headers:
		f.write ("following" + ","),
		#f.write ("timestamp" + ","),

	if "lifeSummary" in headers:
		f.write ("userId" + ","),
		f.write ("displayName" + ","),
		f.write ("status" + ","),
		f.write ("blurb" + ","),
		f.write ("thumbnail" + ","),
		f.write ("image" + ","),
		f.write ("nFollowers" + ","),
		f.write ("vwBirthday" + ","),
		f.write ("nPosts" + ","),
		f.write ("nFollowing" + ","),

	f.write ("\n")

def WriteCommentDataHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	f.write ("\n")
	f.write ("postId" + ","),
	f.write ("userId" + ","),
	f.write ("commentText" + ","),
	f.write ("hashtags" + ","),
	f.write ("timestamp" + ","),
	f.write ("commentId" + ","),
	f.write ("_id" + ","),
	
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")

def WritePostDataHeader (f, output_mode, headers=[], upload=False):
	if (output_mode != 'w') and (output_mode != 'h'):
		return
	
	f.write ("\n")
	f.write ("userId" + ","),
	f.write ("postType" + ","),
	f.write ("nComments" + ","),
	f.write ("nLikes" + ","),
	f.write ("timestamp" + ","),
	f.write ("hashtags" + ","),
	f.write ("postId" + ","),
	f.write ("postText" + ","),
	f.write ("_id" + ","),
	
	if "userDisplayData" in headers:
		f.write ("userDisplayData" + ","),

	f.write ("\n")

def getUserDisplayDataInPosts (post, data_dict, headers):
	try:
		userDisplayData = []
		userDict = data_dict["userDisplayData"]
		if post["postType"] == 3:
			userDisplayData.append (userDict[post["originalPostContent"]["userId"]])

		for each_comment in post["comments"]:
			userDisplayData.append (userDict[each_comment["userId"]])
		headers.append ("userDisplayData")
	except:
		pass
	
	return (headers, userDisplayData)

def getUserDisplayDataInNotifications (notification, data_dict, headers):
	try:
		userDisplayData = []
		userDict = data_dict["userDisplayData"]
		if notification["notificationType"] == 1:
			userDisplayData.append (userDict[notification["followUserId"]])

		headers.append ("userDisplayData")
	except:
		pass
	
	return (headers, userDisplayData)

def getUserDisplayDataInComments (comment, data_dict, headers):
	try:
		userDisplayData = []
		userDict = data_dict["userDisplayData"]
		userDisplayData.append (userDict[comment["userId"]])

		headers.append ("userDisplayData")
	except:
		pass
	
	return (headers, userDisplayData)