#!/usr/bin/env python

#############################################################################################################################################
"""tests_search.py: Search tests for vxwb"""

__author__ = "Gurinder Singh"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer","Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_search = [
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

  ################################################searchUser########################################################
   
  ### 1-1. Search Automation2 User. Status: Done
  #{
  #  "api_name": "1-searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #     "displayName": "Automation2",
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    #"userId":"320888043fdcadcb26c3e341b34fa6221432810135581",
  #    "displayName": "Automation2",
  #    "specific":False,
  #  "should_fail":True,
  #  },
  #},
  #  ##2-1. Partial Search. Status: Done
  #{
  #  "api_name": "2-searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #     "displayName": "Auto",
  #  },
  #  "api_expected":{
  #    "rowcount":17, #Total users with Auto as partial name = 17
  #    "specific":False,
  #  "should_fail":True,
  #  },
  #},
  #
  ###3-1. Blank Search. Status: Done
  #{
  #  "api_name": "3-1-searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #     "displayName": "",
  #  },
  #  "api_store": {
  #    "response": {
  #      "paginationParameter":"paginationParameter",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":20, #Returns all users so 20 on one page
  #    "specific":False,
  #  },
  #},
  #
  #
  ###3-2. Pagination. Status: Done
  #{
  #  "api_name": "3-2-searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #     "displayName": "",
  #     "paginationParameter":"<paginationParameter>"
  #  },    
  #  "api_expected":{
  #    "rowcount":20,
  #    "specific":False
  #  },
  #},
 

  ###4-1. Special character Search. Status: Done
  #{
  #  "api_name": "4-searchUser",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/social/searchUser",
  #  "api_function": "searchUser",
  #  "api_params": {
  #     "displayName": "!@#",
  #  },
  #  "api_expected":{
  #    "rowcount":1, #Returns 1 users
  #    "specific":False,
  #  },
  #},
  
]