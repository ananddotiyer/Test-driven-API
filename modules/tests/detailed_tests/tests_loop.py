#!/usr/bin/env python

#############################################################################################################################################
"""tests_loop.py: Loop tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_loop = [
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

  ################################################getLoop########################################################
  # 1-1. Status: Done
  #{
  #  "api_name": "1-getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #  },
  #  "api_store": {
  #    "response": {
  #      "endPostId":"postId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},
  #
  ## 2-1. Dependent on 1-1. Pagination with valid end post id.  Status: Done
  #{
  #  "api_name": "2-getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #    "endPostId":"<endPostId>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "startPostId":"postId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},
  #
  ## 3-1. Dependent on 2-1. Pagination with valid start post id.  Status: Done
  #{
  #  "api_name": "3-getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #    "startPostId":"<startPostId>"
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},
  #
  ## 3-1. Dependent on 1-1 and 2-1. Pagination with valid start and end post id.  Status: Done
  #{
  #  "api_name": "4-getLoop",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getLoop",
  #  "api_function": "getLoop",
  #  "api_params": {
  #    "startPostId":"<startPostId>",
  #    "endPostId":"<endPostId>"
  #  },
  # "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  }
  #},

]