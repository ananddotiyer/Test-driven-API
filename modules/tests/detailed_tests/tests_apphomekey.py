#!/usr/bin/env python

#############################################################################################################################################
"""tests_appkey_home.py: Appkey Home tests for Network18"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_apphomekey = [
  ################################################Appkey-Home-slug########################################################
  #1-1. 303=Now, Status: Done
  {
    "api_name": "1-appkeyhomeslug",
    "api_type": "POST",
    "api_base_url": "apis/{key}/v3/homeslug/get/1/1/303",
    "api_function": "api_export",
    "api_params": {
      "id_slug": "1",
      "subId_slug": "303",
      "pageNo": 1,
      "app_lang": "2",
      "cat": "",
      "lang": "15"
    },
    "api_expected":{
      "row_json_path": "$.['item'][*]", #all item dicts
      #"row_json_path": "$.['item'][*].['anchors'][*]",#all anchor dicts for all item dicts
      "rowcount":20,
      "call_compare_equals": {
        "$.code": [200],
        "$.['item'][0].['primary_category'][0].['slug']": ["india"]
      },
      "call_compare_types": {
        "$.code": int,
        "$.['item'][0].['primary_category'][0].['slug']": unicode
      },
      "specific":False,
    },
    "api_repl": {
    "key": "bjzlhr11aevxwik0pf0x"
    },    
    "api_store": {
      "response": {
        "$.['item'][0].['primary_category'][0].['slug']": "slug"
      },
    },
    "output_mode": 'w',
  },
]