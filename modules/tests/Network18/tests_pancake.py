#!/usr/bin/env python

#############################################################################################################################################
"""tests_pancake.py: Pancake tests for Network18"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_pancake = [
  ################################################Pancake########################################################
  #1-1. 303=Now, Status: Done
  {
    "api_name": "1-pancake",
    "api_type": "GET",
    "api_base_url": "apis/common/v3/pancake/get/{key}/0/2",
    "api_function": "api_export",
    "api_params": {
    },
    "api_expected":{
      #"row_json_path": "$.['menu'][*]", #all menu dicts
      "row_json_path": "$.['menu'][*].['l2_menu'][*]",#all anchor dicts for all menu dicts
      "rowcount":20,
      "call_compare_equals": {
        "$.code": [200],
      },
      "call_compare_types": {
        "$.code": int,
      },
      "response_schema": "match",
      "specific":False,
    },
    "api_repl": {
    "key": "q1l1fULw5ddj8ysCkDJ8"
    },    
    "api_store": {
      "response": {
      },
    },
    "output_mode": 'w',
  },
]