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
  ################################################Stack-overflow########################################################
  # #1-1. 303=Now, Status: Done
  # {
  #   "api_name": "stackoverflow-search",
  #   "api_type": "GET",
  #   "api_url": "https://api.stackexchange.com/2.2/search/advanced",
  #   "api_function": "api_export",
  #   "api_params": {
  #     "order": "desc",
  #     "sort": "votes",
  #     "site": "stackoverflow",
  #     "tagged": "python",
  #     "accepted": "True",
  #     "title": "how"
  #   },
  #   "api_expected":{
  #     "row_json_path": "$.['items'][*]", #all items dicts
  #     "rowcount":30,
  #     "call_compare_equals": {
  #       "$.['items'][0].['tags'][*]": ["python","python-3.x","dictionary","mapping","idioms"],
  #     },
  #     "call_compare_types": {
  #     },
  #     "response_schema": "write",
  #     "specific":False,
  #   },
  #   "api_repl": {
  #   },    
  #   "api_store": {
  #     "response": {
  #     },
  #   },
  #   "output_mode": 'w',
  # },
  ################################################Google search########################################################
  #1-1. 303=Now, Status: Done
  {
    "api_name": "google-search",
    "api_type": "GET",
    "api_url": "https://www.googleapis.com/customsearch/v1",
    "api_function": "api_export",
    "api_params": {
      "key": "AIzaSyD7x0G_bXAwpd6eXg5NYJn91BLnpkXQ3oE",
      "cx": "002677408965362061794:0wbgub677qo",
      "q": "Anand Iyer",
    },
    "api_expected":{
      "row_json_path": "$.['items'][*]", #all items dicts
      "rowcount":30,
      "call_compare_equals": {
        "$.['items'][0].['title']": ["Anand Iyer | LinkedIn"]
      },
      "call_compare_types": {
      },
      "response_schema": "match",
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