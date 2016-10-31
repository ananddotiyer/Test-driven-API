#!/usr/bin/env python

#############################################################################################################################################
"""tests_social.py: Social tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_social = [
  ################################################/social########################################################
  ## social/uploadContacts.  Status: Done
  #{
  #  "api_name": "uploadContacts",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/uploadContacts",
  #  "api_function": "uploadContacts",
  #  "api_params": {
  #    "contacts": [
  #      {
  #        "phone": "+919999999999"
  #      },
  #      {
  #        "phone": "+918888888888"
  #      }
  #    ]
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    "message":"Contacts processed",
  #    "specific":False
  #  }
  #},
  ## social/getIPContacts.  Status: Done
  #{
  #  "api_name": "getIPContacts",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getIPContacts",
  #  "api_function": "getIPContacts",
  #  "api_params": {
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    "specific":False
  #  }
  #},
  ## social/blockContact.  Status: Done
  #{
  #  "api_name": "blockContact",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/blockContact",
  #  "api_function": "blockContact",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Block successful!",
  #    "specific":False
  #  }
  #},
  ## social/unblockContact.  Status: Done
  #{
  #  "api_name": "unblockContact",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unblockContact",
  #  "api_function": "unblockContact",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unblock successful!",
  #    "specific":False
  #  }
  #},
  ## social/followUser.  Status: Done
  #{
  #  "api_name": "followUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/followUser",
  #  "api_function": "followUser",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Follow Successful!",
  #    "isIPContact":"True",
  #    "specific":False
  #  }
  #},
  ## social/unfollowUser.  Status: Done
  #{
  #  "api_name": "unfollowUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/unfollowUser",
  #  "api_function": "unfollowUser",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Unfollow Successful!",
  #    "specific":False
  #  }
  #},
  ## social/getFollowers.  Status: Done
  #{
  #  "api_name": "getFollowers",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowers",
  #  "api_function": "getFollowers",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":17,
  #    "specific":False
  #  }
  #},
  ## social/getFollowing.  Status: Done
  #{
  #  "api_name": "getFollowing",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/getFollowing",
  #  "api_function": "getFollowing",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},
  ## social/searchUsers.  Status: Done
  #{
  #  "api_name": "searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #    "displayName": "Happy"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
]