#!/usr/bin/env python

#############################################################################################################################################
"""tests_profile.py: Profile tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_profile = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876543210"
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
        "phone": "+919876543210",
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

  ################################################updateProfile########################################################
  ## 1-1. Status: Done
  #{
  #  "api_name": "1-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "Automation",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Profile updated!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 1-2. Status: Done
  #{
  #  "api_name": "1-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "displayName": "Automation",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg",
  #    "specific":False
  #  }
  #},

  ## 2-1. Should return an error.  Seems to be a bug.  Status: Done
  #{
  #  "api_name": "2-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "<error_message>",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 2-2. Should return an error.  Seems to be a bug.  Status: Done
  #{
  #  "api_name": "2-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "displayName": "Automation",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg",
  #    "specific":False
  #  }
  #},

  ## 3-1. Status: Done
  #{
  #  "api_name": "3-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "~!@%%^&**()-+}{][",
  #    "blurb": "~!@%%^&**()-+}{][~!@%%^&**()-+}{][",
  #    "status": "~!@%%^&**()-+}{][~!@%%^&**()-+}{][",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Profile updated!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 3-2. Status: Done
  #{
  #  "api_name": "3-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "displayName": "~!@%%^&**()-+}{][",
  #    "blurb": "~!@%%^&**()-+}{][~!@%%^&**()-+}{][",
  #    "status": "~!@%%^&**()-+}{][~!@%%^&**()-+}{][",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg",
  #    "specific":False
  #  }
  #},

  ## 4-1. Status: Done
  #{
  #  "api_name": "4-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": " ",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Profile updated!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 4-2. Status: Done
  #{
  #  "api_name": "4-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "displayName": " ",
  #    "blurb": "Automation blurb",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg",
  #    "specific":False
  #  }
  #},

  ## 5-1. All spaces.  Status: Done
  #{
  #  "api_name": "5-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": " ",
  #    "blurb": " ",
  #    "status": " ",
  #    "image": " ",
  #    "thumbnail": " "
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Profile updated!",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  ## 5-2. All spaces.  Status: Done
  #{
  #  "api_name": "5-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "displayName": " ",
  #    "blurb": " ",
  #    "status": " ",
  #    "image": " ",
  #    "thumbnail": " ",
  #    "specific":False
  #  }
  #},

  ## 6-1. Blurb is 61 characters.  Returns error, so no ViewProfile done.  Status: Done
  #{
  #  "api_name": "6-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "Automation",
  #    "blurb": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija",
  #    "status": "Automation status",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode": "textLimitExceeded",
  #    "message": "blurb should be under 60 characters.",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},

  ## 7-1. Status is 61 characters.  Returns error, so no ViewProfile done.  Status: Done
  #{
  #  "api_name": "7-updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "Automation",
  #    "blurb": "Automation blurb",
  #    "status": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija",
  #    "image": "http://www.example.com/path/to/profile/automation_image.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/automation_thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode": "textLimitExceeded",
  #    "message": "status should be under 60 characters.",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  ## 8-1. Invalid user.  Status: Done
  #{
  #  "api_name": "8-viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "abcde",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode": "accessTokenInvalid",
  #    "message": "Please check the access token you have entered! Multiple incorrect login attempts will expire the access token!",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
]