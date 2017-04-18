#!/usr/bin/env python

#############################################################################################################################################
"""tests_comment.py: Comment tests for Network18"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_comment = [
  ################################################comment/get########################################################
  # P-1. Status: Done
  {
    "api_name": "1-comment",
    "api_type": "POST",
    "api_url": "http://dev.media.jio.com/n18/apis/common/v3/comment/get",
    "api_function": "api_export",
    "api_params": {
      "article_id":"0023ec30dcbe11e6ab94b53e412a6ed9",
      "user_id":"gl_102780946595724469924",
      "page_number":0
    },
    "api_expected":{
      "row_json_path": "$.['data'][*]",
      "rowcount":2,
      "call_compare_equals": {
        "$.code": [200],
        "$.['data'][0].['user_name']": ["Anand Iyer"],
      },
      "call_compare_types": {
        "$.code": int,
        "$.['data'][0].['user_name']": unicode,
      },
      "response_schema": "match",
      "specific":False,
    },
    "api_repl": {
      "key": "bjzlhr11aevxwik0pf0x"
    },    
    "api_store": {
      "response": {
        "$.['data'][0].['user_name']": "username",
      },
    },
    "output_mode": 'w',
  },
]