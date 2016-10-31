#!/usr/bin/env python

#############################################################################################################################################
"""tests_comment.py: Comment tests for vxwb"""

__author__ = "Gurinder Singh"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer","Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_comment = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500006"
    },
    "api_expected":{
      "rowcount":1,
      "message":"Wait for text message!",
      "specific":False,
    },
    "output_mode": 'n',
  },
  # P-2. Status: Done
  {
    "api_name": "P-2-getAccessToken",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getAccessToken",
    "api_function": "getAccessToken",
    "api_params": {
        "phone": "+919876500006",
        "verificationCode" : "111111"
    },
    "api_store": {
      "response": {
        "userId":"userId",
      },
    },
    "api_expected":{
      "rowcount":1,
      "message": "Verification successful!",
      "specific":False
    },
  },

  ################################################uploadComment########################################################
  
  ### 1-1. Upload comment to automation7. Status: Done.
  #{
  #  "api_name": "1-uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #     "postId": "14d9fc2a4d9JuhT8R91Ht92LVTqmGnsrk",
  #     "userId":"b0d0a85459a08e844091b78481812a081432810381979",
  #     "commentText":"Just another comment via automation"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postId":"14d9fc2a4d9JuhT8R91Ht92LVTqmGnsrk",
  #    "userId": "<userId>",
  #    "commentObject/postId":"14d9fc2a4d9JuhT8R91Ht92LVTqmGnsrk",
  #    "commentObject/userId": "<userId>",
  #    "message": "Comment added successfully!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 2-1.Blank PostId. Status: Done. Check why not printing Success.
  #{
  #  "api_name": "2-uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #     "postId": "",
  #     "userId":"b0d0a85459a08e844091b78481812a081432810381979",
  #     "commentText":"Just another comment via automation"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message": "The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 3-1.Blank UserId. Status: Done. Bug Fix Needed.
  #{
  #  "api_name": "3-uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #     "postId": "14d9fc2a4d9JuhT8R91Ht92LVTqmGnsrk",
  #     "userId":"",
  #     "commentText":"Just another comment via automation"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "message": "The specified userId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 4-1.invalid PostId. Status: Done.
  #{
  #  "api_name": "4-uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #     "postId": "sleiugvehoiievmgoervm",
  #     "userId":"b0d0a85459a08e844091b78481812a081432810381979",
  #     "commentText":"Just another comment via automation"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message": "The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 5-1.Invalid UserId. Status: Done. Bug Fix Needed.
  #{
  #  "api_name": "5-uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #     "postId": "14d9fc2a4d9JuhT8R91Ht92LVTqmGnsrk",
  #     "userId":"kdfgncgcumocye",
  #     "commentText":"Just another comment via automation"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "message": "The specified userId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  
################################################getPostComments########################################################
### 1-1. Upload comment to automation7. Status: Done.
#  {
#    "api_name": "1-getPostComments",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/life/getPostComments",
#    "api_function": "getPostComments",
#    "api_params": {
#       "postId": "14d48aceef0q_A1ZoW2HCDesq3CH0NSZk",
#    },
#    "api_expected":{
#      "rowcount":4,
#      "postId": "14d48aceef0q_A1ZoW2HCDesq3CH0NSZk",
#      "specific":False,
#    },
#  },
  
### 2-1. Pagination. Status: Done.
#  {
#    "api_name": "2-getPostComments",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/life/getPostComments",
#    "api_function": "getPostComments",
#    "api_params": {
#       "postId": "14dc2604c59M3DgTg2_FCioPOXIModycV",
#    },
#    "api_store": {
#      "response": {
#        "commentId":"commentId",
#      },
#    },      
#    "api_expected":{
#      "rowcount":20,
#      "specific":False,
#    },
#  },
# ## 2-2. Pagination. Status: Done.
#  {
#    "api_name": "2-2-getPostComments",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/life/getPostComments",
#    "api_function": "getPostComments",
#    "api_params": {
#       "postId": "14dc2604c59M3DgTg2_FCioPOXIModycV",
#       "endCommentId":"<commentId>",
#    },
#    "api_expected":{
#      "rowcount":19,
#      "specific":False,
#    },
#  },  
 
  ### 3-1. Get Comment. PostId blank. Status: Done.
  #{
  #  "api_name": "3-getPostComments",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostComments",
  #  "api_function": "getPostComments",
  #  "api_params": {
  #     "postId": "",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message": "The specified postId could not be found in the database",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 4-1. Get Comment. PostId invalid. Status: Done.
  #{
  #  "api_name": "4-getPostComments",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostComments",
  #  "api_function": "getPostComments",
  #  "api_params": {
  #     "postId": "askufycgnufygeu",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message": "The specified postId could not be found in the database",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
]