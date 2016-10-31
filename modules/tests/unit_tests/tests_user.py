#!/usr/bin/env python

#############################################################################################################################################
"""tests_user.py: User tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_user = [
  ################################################/user########################################################
  # user/getVerificationCode.  Status: Done
  {
    "api_name": "getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
        "phone": "+919845177582"
    },
    "api_expected":{
      "rowcount":1,
      "message":"Wait for text message!",
      "specific":False
    }
  },
  # user/getAccessToken.  Status: Done
  {
    "api_name": "getAccessToken",
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
      "isNewUser": "False",
      "specific":False
    }
  },
  ## user/getCognitoToken.  Status: Done
  #{
  #  "api_name": "getCognitoToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getCognitoToken",
  #  "api_function": "getCognitoToken",
  #  "api_params": {
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## user/updateProfile.  Status: Done
  #{
  #  "api_name": "updateProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/updateProfile",
  #  "api_function": "updateProfile",
  #  "api_params": {
  #    "displayName": "Happy Waters",
  #    "blurb": "I'm Moolya's test architect",
  #    "status": "User's feelings in under 60 characters",
  #    "image": "http://www.example.com/path/to/profile/picture.jpg",
  #    "thumbnail": "http://www.example.com/path/to/profile/picture/thumbnail.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Profile updated!",
  #    "specific":False
  #  }
  #},
  ## user/viewProfile.  Status: Done
  #{
  #  "api_name": "viewProfile",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/viewProfile",
  #  "api_function": "viewProfile",
  #  "api_params": {
  #    "userId": "<userId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## user/getNotifications.  First 20.  Status: Done
  #{
  #  "api_name": "getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #  },
  #  "api_store": {
  #    "response": {
  #      "notificationId":"notificationId",
  #      "userId":"followUserId",#last followUserId in the list of dictionaries
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "specific":False
  #  }
  #},
  ## user/getLoop.  First 20.  Status: Done
  #{
  #  "api_name": "getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId1":"postId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},
  ## user/getLoop.  Next 20.  Status: Done
  #{
  #  "api_name": "getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #    "endPostId": "<postId1>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId2":"postId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  },
  #  "output_mode": "h",
  #},

]