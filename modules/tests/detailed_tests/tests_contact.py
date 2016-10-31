#!/usr/bin/env python

#############################################################################################################################################
"""tests_contact.py: Contact tests for vxwb"""

__author__ = "Gurinder Singh"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer","Gurinder Singh"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_contact = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500111"
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
        "phone": "+919876500111",
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

################################################uploadContacts########################################################
#  # 1-1. Valid Contact Numbers. Status: Done.
#   {
#     "api_name": "1-uploadContacts",
#     "api_type": "POST",
#     "api_base_url": "/api/v1/social/uploadContacts",
#     "api_function": "uploadContacts",
#     "api_params": {
#       "contacts": [
#         {
#           "phone": "+917766554433"
#         },
#         {
#           "phone": "+917766554434"
#         }
#       ]
#     },
#     "api_expected":{
#       "rowcount":2,
#       "parseStatus":"4",
#       "message":"Contacts processed",
#       "specific":False,
#     },
#   },
#   
#  ## 2-1. Contact Number Blank. Status: Done.
#  {
#    "api_name": "2-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": ""
#        },
#        {
#          "phone": ""
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":2,
#      "parseStatus":"1",
#      "message":"Contacts processed",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#  ## 3-1. Contact Number Invalid. Status: Done.
#  {
#    "api_name": "3-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": "91221"
#        },
#        {
#          "phone": "832457"
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":2,
#      "parseStatus":"1",
#      "message":"Contacts processed",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#   
#  # 4-1. Contact Number Valid and Same. Status: Done.
#  {
#    "api_name": "4-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": "+919988987676"
#        },
#        {
#          "phone": "+919988987676"
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":2,
#      "parseStatus":"4",
#      "message":"Contacts processed",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },  
#  
#  ## 5-1. Contact Number Same and Country code absent in one. Status: Done.
#  {
#    "api_name": "5-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": "+919988987898"
#        },
#        {
#          "phone": "9988987898"
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":2,
#      "message":"Contacts processed",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#  ## 6-1. Own Contact number. Status: Done.
#  {
#    "api_name": "6-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": "+917770011111"
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":1,
#      "parseStatus":"2",
#      "message":"Contacts processed",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#  ## 7-1. Multiple Contacts. Status: Done.
#  {
#    "api_name": "7-uploadContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/uploadContacts",
#    "api_function": "uploadContacts",
#    "api_params": {
#      "contacts": [
#        {
#          "phone": "+917779878811"
#        },
#        {
#          "phone": "+917779878812"
#        },
#        {
#          "phone": "+917779878813"
#        },
#        {
#          "phone": "+917779878814"
#        },
#        {
#          "phone": "+917779878815"
#        },
#        {
#          "phone": "+917779878816"
#        }
#      ]
#    },
#    "api_expected":{
#      "rowcount":6,
#      "parseStatus":"4",
#      "message":"Contacts processed",
#      "specific":False,
#    },
#  },
#   
# ###############################################getIPContacts########################################################
# 
#   ## 1-1. Status: Add row count after configuring pre condition
#   {
#     "api_name": "1-getIPContacts",
#     "api_type": "POST",
#     "api_base_url": "/api/v1/social/getIPContacts",
#     "api_function": "getIPContacts",
#     "api_params": {
#     },
#     "api_expected":{
#       "rowcount":15,
#       "specific":False,
#     },
#   },
#   
#   ## 2-1. Pagination : Invalid character. Status: Done.
#   {
#     "api_name": "2-getIPContacts",
#     "api_type": "POST",
#     "api_base_url": "/api/v1/social/getIPContacts",
#     "api_function": "getIPContacts",
#     "api_params": {
#       "paginationParameter": "10" 
#     },
#     "api_expected":{
#       "rowcount":5,
#       "specific":False,
#     },
#     "output_mode": 'n',
#   }, 
#  
#  ## 3-1. Pagination : Invalid character. Status: Done.
#  {
#    "api_name": "3-getIPContacts",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/getIPContacts",
#    "api_function": "getIPContacts",
#    "api_params": {
#      "paginationParameter": "$$" 
#    },
#    "api_expected":{
#      "rowcount":0,
#      "message":"There was an error in our database. Please try again.",
#      "errorCode": "databaseError",      
#      "specific":False,
#      "should_fail":True,
#    },
#    "output_mode": 'n',
#  }, 
#  
#################################################blockContact########################################################
#  
#  ## 1-1. Status: Add USERID in param
#  {
#    "api_name": "1-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "message":"Block successful!",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#    ## 2-1. Invalid UserID. Status: BUG FIX REQUIRED. ADJUST API_EXPECTED.
#  {
#    "api_name": "2-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": "1234567876543211234567890987654321234rhegfghf"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#  ## 3-1. Blank UserID. Status: BUG FIX REQUIRED. ADJUST API_EXPECTED.
#  {
#    "api_name": "3-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": ""
#      },
#    "api_expected":{
#      "rowcount":1,
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#  ## 4-1. Already Blocked UserID. Status: BUG FIX REQUIRED. ADJUST API_EXPECTED.
#  {
#    "api_name": "4-2-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },  
#  
#  ## 5-1. Own UserID. Status: BUG FIX REQUIRED. ADJUST API_EXPECTED.
#  {
#    "api_name": "5-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": "<userId>"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
#   ## 6-1. Status: Add USERID in param
#   {
#     "api_name": "6-blockContact",
#     "api_type": "POST",
#     "api_base_url": "/api/v1/social/blockContact",
#     "api_function": "blockContact",
#     "api_params": {
#       "userd": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#       },
#     "api_expected":{
#       "rowcount":0,
#       "message": "Required parameter userId missing",
#       "errorCode": "syntaxError",
#       "specific":False,
#       "should_fail":True,
#     },
#     "output_mode": 'n',
#   },  
#    
#################################################unblockContact########################################################
#  
#  ## 1-1. Status: Add USERID in param
#  {
#    "api_name": "P-1-blockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/blockContact",
#    "api_function": "blockContact",
#    "api_params": {
#      "userId": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "message":"Block successful!",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },  
#  ## 1-2. Unblock Contact. Status: UserId to be mapped.
#  {
#    "api_name": "1-unblockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/unblockContact",
#    "api_function": "unblockContact",
#    "api_params": {
#      "userId": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "message":"Unblock successful!",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
#  
### 2-1. Unblock invalid UserId. Status: Bug Fix Needed. Update api_expected when fixed.
#  {
#    "api_name": "2-unblockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/unblockContact",
#    "api_function": "unblockContact",
#    "api_params": {
#      "userId": "dsfhvrvrtverthvrethrtver"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "message":"",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },  
#
### 3-1. Unblock non-bocked UderId. Status: Update userId. Bug Fix Needed. Update api_expected when fixed.
#  {
#    "api_name": "3-unblockContact",
#    "api_type": "POST",
#    "api_base_url": "/api/v1/social/unblockContact",
#    "api_function": "unblockContact",
#    "api_params": {
#      "userId": "421ea372dd5a438889a1e2e5350a4a611431322463144"
#      },
#    "api_expected":{
#      "rowcount":1,
#      "message":"",
#      "specific":False,
#    },
#    "output_mode": 'n',
#  },
# 
#   ## 4-1. Unblock Contact. Status: UserId to be mapped.
#   {
#     "api_name": "4-unblockContact",
#     "api_type": "POST",
#     "api_base_url": "/api/v1/social/unblockContact",
#     "api_function": "unblockContact",
#     "api_params": {
#       "userd": "7bcce99da67c3e84f40b38f1d5422eea1432701603331"
#       },
#     "api_expected":{
#       "rowcount":0,
#       "message": "Required parameter userId missing",
#       "errorCode": "syntaxError",
#       "specific":False,
#       "should_fail":True,
# 
#     },
#     "output_mode": 'n',
#   },
# #  
]