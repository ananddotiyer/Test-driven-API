#!/usr/bin/env python

#############################################################################################################################################
"""tests_like.py: Like tests for vxwb"""

__author__ = "Gurinder Singh"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer","Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_like = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500001"
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
        "phone": "+919876500001",
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

  ################################################uploadLike########################################################
  ### 1-1. Status: Done. User: Automation5.
  # {
  #    "api_name": "1-uploadLike",
  #    "api_type": "POST",
  #    "api_base_url": "/api/v1/life/uploadLike",
  #    "api_function": "uploadLike",
  #    "api_params": {
  #      "postId": "14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #      "userId":"320888043fdcadcb26c3e341b34fa6221432810135581"
  #    },
  #    "api_expected":{
  #      "rowcount":1,
  #      "message": "Post liked!",
  #      "specific":False,
  #    },
  #    "output_mode": 'n',
  #  },   
  ### 1-2. Getting Post and Checking if Liked. User: Automation5.  Status: Done.
  #{
  #  "api_name": "1-2-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "14d9a4ffb34PKnBtYz1GdTg51zKWQBijF"
  #    },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postObject/isLiked/isLiked" : "True",
  #    "specific":False,
  #    }
  #},
  
  ### 2-1. Invalid PostId Valid UserId. Status: Done.
  #{
  #  "api_name": "2-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #     "postId":"iuegnvughmiveghueuh",
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message":"The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},

  ### 3-1. Valid PostId Invalid UserId. Status: Bug Fix Required. Update expected after fix.
  #{
  #  "api_name": "3-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #     "postId":"14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #     "userId": "uyefgneugcfif",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "message":"The specified userId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  # 
  ### 4-1.  PostId and UserId Invalid. Status: Done.
  #{
  #  "api_name": "4-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #     "postId":"ksajfaskcfbasjhasl",
  #     "userId": "uyefgneugcfif",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message":"The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  # 
  ### 5-1.  PostId and UserId Blank. Status: Done.
  #{
  #  "api_name": "5-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #     "postId":"",
  #     "userId": "",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "message":"The specified postId could not be found in the database",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
    
 ################################################deleteLike########################################################
 
  ### 1-1. Status: Done. User: Automation5.
  #{
  #  "api_name": "1-1-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #     "postId":"14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post liked!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ### 1-2. Status: Some code problem.
  #{
  #  "api_name": "1-2-deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #     "postId":"14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post unliked!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},

  ### 2-1. PostId Invalid. Status: Bug Fix Required. Modify expected accordingly.
  #{
  #  "api_name": "2-deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #     "postId":"ubiyfbiunfufufiu",
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"postIdInvalid",
  #    "specific":False,
  #    "should_fail":True,
  #
  #  },
  #  "output_mode": 'n',
  #},
  #  
  ### 3-1. UserId Invalid. Status: Bug Fix Required. Modify expected accordingly.
  #{
  #  "api_name": "3-deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #     "postId":"14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #     "userId": "evefvvevevev",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "specific":False,
  #    "should_fail":True,
  #
  #  },
  #  "output_mode": 'n',
  #},
  #  
  ### 4-1. Both ID Invalid. Status: Bug Fix Required. Modify expected accordingly.
  #{
  #  "api_name": "4-deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #     "postId":"14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #     "userId": "evefvvevevev",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #  
  ### 5-1. Both ID Blank. Status: Bug Fix Required. Modify expected accordingly.
  #{
  #  "api_name": "4-deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #     "postId":"",
  #     "userId": "",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"userIdInvalid",
  #    "specific":False,
  #    "should_fail":True,
  #
  #  },
  #  "output_mode": 'n',
  #},
   
  ################################################getPostLikes########################################################

  ### 1-1. Status: Done. User: Automation5.
  #{
  #  "api_name": "1-uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #    "postId": "14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #    "userId":"320888043fdcadcb26c3e341b34fa6221432810135581"
  #  },
  #  "api_store": {
  #    "response": {
  #    "likeId":"likeId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Post liked!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ### 1-2. Status: Done. User: Automation5.
  #{
  #  "api_name": "1-getPostLikes",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostLikes",
  #  "api_function": "getPostLikes",
  #  "api_params": {
  #    "postId": "14d9a4ffb34PKnBtYz1GdTg51zKWQBijF",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "likeId" : "<likeId>",
  #    "displayName": "Automation1",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  
 # ## 2-1. Pagination
 #{
 #  "api_name": "2-getPostLikes",
 #  "api_type": "POST",
 #  "api_base_url": "/api/v1/life/getPostLikes",
 #  "api_function": "getPostLikes",
 #  "api_params": {
 #    "postId": "14dc2604c59M3DgTg2_FCioPOXIModycV"
 #  },
 #  "api_store": {
 #    "response": {
 #      "likeId":"likeId",
 #    },
 #  },
 #  "api_expected":{
 #    "rowcount":20,
 #    "specific":False,
 #  },
 #},
 ### 2-2. Pagination
 #{
 #  "api_name": "2-2-getPostLikes",
 #  "api_type": "POST",
 #  "api_base_url": "/api/v1/life/getPostLikes",
 #  "api_function": "getPostLikes",
 #  "api_params": {
 #    "postId": "14dc2604c59M3DgTg2_FCioPOXIModycV",
 #    "endLikeId": "<likeId>",
 #  },  
 #  "api_expected":{
 #    "rowcount":1,
 #    "specific":False,
 #  },
 #},
 
  ### 3-1. Invalid PostId. Status: Bug Fix. no error Code. Returns empty list. . User: Automation5.
  #{
  #  "api_name": "3-getPostLikes",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostLikes",
  #  "api_function": "getPostLikes",
  #  "api_params": {
  #    "postId": "dgvyryryry",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  # 
  #    
  ### 4-1. Empty PostId. Status: Bug Fix. no error Code. Returns empty list. . User: Automation5.
  #{
  #  "api_name": "4-getPostLikes", 
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostLikes",
  #  "api_function": "getPostLikes",
  #  "api_params": {
  #    "postId": "",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
]