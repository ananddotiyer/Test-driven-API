#!/usr/bin/env python

#############################################################################################################################################
"""tests_token.py: Toekn tests for Wally"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_token = [
  ################################################Appkey-Home-slug########################################################
  #1-1. 303=Now, Status: Done
  {
    "api_name": "1-refreshtoken",
    "api_type": "POST",
    "api_base_url": "oauth/token",
    "api_function": "api_export",
    "api_params": {
      "client_id": "cMQgd64KSJrkKM0zDCIFzL8PeYJoUzU1",
      "grant_type": "refresh_token",
      "refresh_token": "YPzcEI9fmAb5tZycyFNr4xwdTYXtvuqL"
    },
    "api_expected":{
      "row_json_path": "",
      "rowcount":1,
      "specific":False,
    },
    "api_repl": {
    },    
    "api_store": {
      "response": {
        "$[0].['access_token']": "token"
      },
    },
    "output_mode": 'n',
  },
  #1-1. 303=Now, Status: Done
  {
    "api_name": "1-currentuser",
    "api_type": "GET",
    "api_base_url": "users/current",
    "api_function": "api_export",
    "api_params": {
    },
    "api_headers": {
      "Authorization": "Bearer <token>"
    },
    "api_expected":{
      "row_json_path": "",
      "rowcount":1,
      "specific":False,
    },
    "api_repl": {
    },    
    "api_store": {
      "response": {
      },
    },
    "output_mode": 'w',
  },

]