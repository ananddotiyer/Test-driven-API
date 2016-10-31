#!/usr/bin/env python

#############################################################################################################################################
"""tests_lifepage.py: Life page tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_lifepage = [
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

  ################################################getLifePage########################################################
  ## 1-1. Status: Done
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
  #      "endPostId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":15,
  #    "specific":False
  #  }
  #},
  #
  ## 2-1. Dependent on 1-1. Pagination with valid end post id.  Status: Done
  #{
  #  "api_name": "2-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "endPostId": "<endPostId>",
  #  },
  #  "api_store": {
  #    "response": {
  #      "startPostId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":3,
  #    "specific":False
  #  }
  #},
  #
  ## 3-1. Dependent on 1-1. Pagination with valid end postId and empty start postId.  Status: Done
  #{
  #  "api_name": "3-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "startPostId": "",
  #    "endPostId": "<endPostId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  #
  ## 4-1. Dependent on 2-1. Pagination with valid start post id.  Status: Done
  #{
  #  "api_name": "4-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "startPostId": "<startPostId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  #
  ## 5-1. Dependent on 2-1. Pagination with valid start postId and blank end postId.  14 posts expected, but 0 found.  Could be a bug. Status: Done
  #{
  #  "api_name": "5-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "startPostId": "<startPostId>",
  #    "endPostId": "",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  #
  ## 6-1. Dependent on 1-1 and 2-1. Pagination with valid start and end post id.  Status: Done
  #{
  #  "api_name": "6-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "startPostId": "<startPostId>",
  #    "endPostId": "<endPostId>",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  #
  ## 7-1. Dependent on 1-1 and 2-1. Pagination with invalid start and end post id.  Status: Done
  #{
  #  "api_name": "7-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "startPostId": "abcd",
  #    "endPostId": "abcd",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False
  #  }
  #},
  #
  ## 8-1. Dependent on 1-1 and 2-1. Invalid userId. Status: Done
  #{
  #  "api_name": "8-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "abcd",
  #    "startPostId": "<startPostId>",
  #    "endPostId": "<endPostId>",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False
  #  }
  #},
  #
  ## 9-1. Single posttype.  Status: Done
  #{
  #  "api_name": "9-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "postType": "5"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  #
  ## 10-1. Multiple posttypes.  Status: Done
  #{
  #  "api_name": "9-getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>",
  #    "postType": "[1,5]"
  #  },
  #  "api_expected":{
  #    "rowcount":15,
  #    "specific":False
  #  }
  #},

]