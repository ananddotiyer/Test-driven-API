#!/usr/bin/env python

#############################################################################################################################################
"""tests_follow.py: Follow tests for vxwb"""

__author__ = "Gurinder Singh"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer","Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_follow = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500003"
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
        "phone": "+919876500003",
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

  ################################################followUser########################################################
  ## 1-1. Following Contact User. Status: Done
  #{
  #  "api_name": "1-followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #     "userId": "7c04d4383972ba652fc874b5685dbc481432810174440",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Follow Successful!",
  #    "isIPContact": 'True',       
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  # 
  ## 2-1. Following Non-Contact User. Status: Done.
  #{
  #  "api_name": "2-followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #     "userId": "b0d0a85459a08e844091b78481812a081432810381979",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Follow Successful!",
  #    "isIPContact": 'False',
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
   
  ## 3-1. InvalidUserId. Status: Done.
  #{
  #  "api_name": "3-followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #     "userId": "8octn238t823cb83cnt83gtn32ox7823on",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "message":"There was an error in our database. Please try again.",
  #    "errorCode":"databaseError",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 4-1. Follow Self. Status: Done.
  #{
  #  "api_name": "4-followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #     "userId": "<userId>",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "message":"You cannot follow yourself. That's illogical!",
  #    "errorCode":"selfFollowAttempt",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
     
  ################################################unfollowUser########################################################
  ## 1-1. Following Non-Contact User.
  #{
  #  "api_name": "1-followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #     "userId": "b0d0a85459a08e844091b78481812a081432810381979",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Follow Successful!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ## 1-2. unfollow User. Status: Done.
  #{
  #  "api_name": "1-unfollowUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unfollowUser",
  #  "api_function": "unfollowUser",
  #  "api_params": {
  #     "userId": "b0d0a85459a08e844091b78481812a081432810381979",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unfollow Successful!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  # 
  ## 2-1. unfollow Invalid userId. Status: Bug Fix Required. Update expected when fixed.
  #{
  #  "api_name": "2-unfollowUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unfollowUser",
  #  "api_function": "unfollowUser",
  #  "api_params": {
  #     "userId": "ocgnoeygmoygeytemoyger",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unfollow Successful!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
   
   
  ## 3-1. unfollow not Followed userId. Status: Bug Fix Required. Update expected when fixed.
  #{
  #  "api_name": "3-unfollowUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unfollowUser",
  #  "api_function": "unfollowUser",
  #  "api_params": {
  #     "userId": "1b64595b75b4f9aa85b520f764d2dc5f1432810502849",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unfollow Successful!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 4-1. Unfollow Self. Status: Bug Fix Required. Update expected when fixed.
  #{
  #  "api_name": "4-unfollowUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unfollowUser",
  #  "api_function": "unfollowUser",
  #  "api_params": {
  #     "userId": "<userId>",
  # },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unfollow Successful!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
   
  ################################################getFollowers########################################################

  ## 1-1. Pagination.  Status: Done
  #{
  #  "api_name": "1-getFollowers",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowers",
  #  "api_function": "getFollowers",
  #  "api_params": {
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_store": {
  #    "response": {
  #      "paginationParameter":"paginationParameter",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":4,
  #    "specific":False,
  #  },
  #},
  #
  ## 2-1. Pagination. Status: Done
  #{
  #  "api_name": "2-getFollowers",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowers",
  #  "api_function": "getFollowers",
  #  "api_params": {
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #     "paginationParameter": "<paginationParameter>",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  
  ## 3-1. Blank userId.  Status: Done
  #{
  #  "api_name": "3-getFollowers",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowers",
  #  "api_function": "getFollowers",
  #  "api_params": {
  #     "userId": "",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  #    
  ## 4-1. Invalid UserID. Status: Done
  #{
  #  "api_name": "4-getFollowers",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowers",
  #  "api_function": "getFollowers",
  #  "api_params": {
  #     "userId": "onegwocrmyeygeomcgyeorygcmy",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #}, 
   
  ################################################getFollowing########################################################
 
  ## 1-1. Pagination.  Status: Done
  #{
  #  "api_name": "1-getFollowing",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowing",
  #  "api_function": "getFollowing",
  #  "api_params": {
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #  },
  #  "api_store": {
  #    "response": {
  #      "paginationParameter":"paginationParameter",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":4,
  #    "specific":False,
  #  },
  #},
  #
  ## 2-1. Pagination. Bug.  'There was an error in our database. Please try again.' Status: Done
  #{
  #  "api_name": "2-getFollowing",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowing",
  #  "api_function": "getFollowing",
  #  "api_params": {
  #     "userId": "320888043fdcadcb26c3e341b34fa6221432810135581",
  #     "paginationParameter": "<paginationParameter>",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  
  ## 3-1. Invalid UserId. Status: Done
  #{
  #  "api_name": "3-getFollowing",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowing",
  #  "api_function": "getFollowing",
  #  "api_params": {
  #     "userId": "o8eyfgecnt248t7g248tg8tgm8t",
  # },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
 
]