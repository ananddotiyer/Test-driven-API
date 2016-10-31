#!/usr/bin/env python

#############################################################################################################################################
"""tests_lifepost.py: Life post tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_lifepost = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919845177582"
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
        "phone": "+919845177582",
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

  ################################################getLifePage, deleteLifePost, getLifePost######################################################
  ## 1-1. Delete the last post returned in life page, and check if it can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "1-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":15,
  #    "specific":False
  #  }
  #},
  ## 1-2. Delete the last post returned in life page, and check if it can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "1-deleteLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLifePost",
  #  "api_function": "deleteLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post deleted!",
  #    "specific":False
  #  }
  #},
  ## 1-3. Delete the last post returned in life page, and check if it can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "1-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message":"The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},  
  #
  ## 2-1. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":15,
  #    "specific":False
  #  }
  #},
  ## 2-2. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-2-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+919876543210"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Wait for text message!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ## 2-3. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-3-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "111111"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Verification successful!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 2-4. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "errorCode":"postIdInvalid",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},  
  ## 2-5. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-5-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+919845177582"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Wait for text message!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ## 2-6. Check if another user's post can't be retrieved in getLifePost.  Status: Done
  #{
  #  "api_name": "2-6-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919845177582",
  #      "verificationCode" : "111111"
  #  },
  #  "api_store": {
  #    "response": {
  #      "userId":"userId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Verification successful!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 3-1. Upload two posts.  getLifePost for both postIds.  Status: Done
  #{
  #  "api_name": "3-1-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Text post-1"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId1":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 3-2. Upload two posts.  getLifePost for both postIds.  Status: Done
  #{
  #  "api_name": "3-2-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Text post-2"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId2":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 3-3. Upload two posts.  getLifePost for both postIds.  Status: Done
  #{
  #  "api_name": "3-3-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "[\"<postId1>\",\"<postId2>\"]"
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    "specific":False,
  #  }
  #},  
  #
  ## 3-4. Dependent on 3-1 and 3-2.  Upload two posts.  getLifePost for both postIds in addition to an invalid postId.  Status: Done
  #{
  #  "api_name": "3-4-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "[\"<postId1>\",\"<postId2>\",\"abcd\"]"
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    "specific":False,
  #  },
  #},  

]