#!/usr/bin/env python

#############################################################################################################################################
"""tests_misc.py: Misc tests from lot of servers"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_misc = [
  ################################################Appkey-Home-slug########################################################
  #1-1. 303=Now, Status: Done
  {
    "api_name": "1-misc",
    "api_type": "GET",
    "api_base_url": "search/advanced",
    "api_function": "api_export",
    "api_params": {
      "order": "desc",
      "sort": "votes",
      "site": "stackoverflow",
      "tagged": "python",
      "accepted": "True",
      "title": "how"
    },
    "api_expected":{
      "row_json_path": "$.['items'][*]", #all items dicts
      "rowcount":30,
      "call_compare_equals": {
        "$.['items'][0].['tags'][*]": ["python","python-3.x","dictionary","mapping","idioms"],
      },
      "call_compare_types": {
      },
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