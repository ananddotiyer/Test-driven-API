#!/usr/bin/env python

#############################################################################################################################################
"""tests_authentication.py: Authentication tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_authentication = [
  ################################################getVerificationCode########################################################
  ## 1-1. Status: Done
  #{
  #  "api_name": "1-getVerificationCode",
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

  ## 2-1. Status: Done
  #{
  #  "api_name": "2-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+91"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "httpStatus": "400",
  #    "message":"Please enter a valid E.164 phone number.",
  #    "errorCode":"phoneNumberFormatError",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},

  ## 3-1. Status: Done
  #{
  #  "api_name": "3-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+91$$$$$$$$$$"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "httpStatus": "400",
  #    "message":"Please enter a valid E.164 phone number.",
  #    "errorCode":"phoneNumberFormatError",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  
  ## 4-1. Status: Done
  #{
  #  "api_name": "4-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+91abcdefghij"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "httpStatus": "400",
  #    "message":"Please enter a valid E.164 phone number.",
  #    "errorCode":"phoneNumberFormatError",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},
  
  ## 5-1. Status: Done
  #{
  #  "api_name": "5-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": ""
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "httpStatus": "400",
  #    "message":"Please enter a valid E.164 phone number.",
  #    "errorCode":"phoneNumberFormatError",
  #    "specific":False,
  #    "should_fail":True,
  #  },
  #  "output_mode": 'n',
  #},

  ################################################getVerificationCode,getAccessToken########################################################
  ## 1-1. isNewUser is True.  Register a new user.  Status: Done
  #{
  #  "api_name": "1-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+919876543101"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Wait for text message!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ## 1-2.  isNewUser is True.  Register a new user.  Status: Done
  #{
  #  "api_name": "1-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543101",
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
  #    "isNewUser": "True",
  #    "specific":False
  #  },
  #},

  ## 2-1. isNewUser is False. Status: Done.
  #{
  #  "api_name": "2-getVerificationCode",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getVerificationCode",
  #  "api_function": "getVerificationCode",
  #  "api_params": {
  #    "phone": "+919876543101"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Wait for text message!",
  #    "specific":False,
  #  },
  #  "output_mode": 'n',
  #},
  ## 2-2. isNewUser is False.  Status: Done
  #{
  #  "api_name": "2-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543101",
  #      "verificationCode" : "111111"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message": "Verification successful!",
  #    "isNewUser": "False",
  #    "specific":False
  #  },
  #},

  ## 3-1. Status: Done
  #{
  #  "api_name": "3-getVerificationCode",
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
  ## 3-2.  Status: Done
  #{
  #  "api_name": "3-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : ""
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},

  ## 4-1. Status: Done
  #{
  #  "api_name": "4-getVerificationCode",
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
  ## 4-2.  Status: Done
  #{
  #  "api_name": "4-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "1"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},

  ## 5-1. Status: Done
  #{
  #  "api_name": "5-getVerificationCode",
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
  ## 5-2.  Status: Done
  #{
  #  "api_name": "5-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "%"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 6-1. Status: Done
  #{
  #  "api_name": "6-getVerificationCode",
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
  ## 6-2.  Status: Done
  #{
  #  "api_name": "6-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "&&&&&&"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 7-1. Status: Done
  #{
  #  "api_name": "7-getVerificationCode",
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
  ## 7-2.  Status: Done
  #{
  #  "api_name": "7-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "11111111"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 8-1. Verification code contains one space.  Status: Done
  #{
  #  "api_name": "8-getVerificationCode",
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
  ## 8-2.  Verification code contains one space.  Status: Done
  #{
  #  "api_name": "8-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : " "
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 9-1. Verification code contains multiple spaces.  Status: Done
  #{
  #  "api_name": "9-getVerificationCode",
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
  ## 9-2.  Verification code contains multiple spaces.  Status: Done
  #{
  #  "api_name": "9-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "      "
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification code incorrect. Try again.",
  #    "errorCode": "verificationCodeIncorrect",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},

  ## 10-1. Number for which "getVerificationCode" not executed.  New Number.  Status: Done
  #{
  #  "api_name": "10-getVerificationCode",
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
  ## 10-2.  Number for which "getVerificationCode" not executed.  New Number.  Status: Done
  #{
  #  "api_name": "10-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543100",#number is not registered
  #      "verificationCode" : "111111"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Phone number was not found in database. Maybe you should register first ?",
  #    "errorCode": "phoneNumberInvalid",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
  
  ## 11-2.  Number for which "getVerificationCode" not executed.  Already registered number.  Status: Done
  #{
  #  "api_name": "11-getAccessToken",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getAccessToken",
  #  "api_function": "getAccessToken",
  #  "api_params": {
  #      "phone": "+919876543210",
  #      "verificationCode" : "111111"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "httpStatus": "400",
  #    "message": "Verification Code is expired. Get a new verification code.",
  #    "errorCode": "verificationCodeExpired",
  #    "specific":False,
  #    "should_fail":True
  #  },
  #  "output_mode": 'n',
  #},
 
 
   ################################################/user/getCognitoToken########################################################
  ## 1-1.  Status: Not Done
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
  #  },
  #  "output_mode": 'n',
  #},
]