#!/usr/bin/env python

#############################################################################################################################################
"""tests_notifications.py: Notification tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_notifications = [
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

  ################################################getNotifications########################################################
  ## 1-1. Status: Done
  #{
  #  "api_name": "1-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #  },
  #  "api_store": {
  #    "response": {
  #      "endnotificationId":"notificationId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 2-1. Dependent on 1-1. Pagination with valid end notification id.  Status: Done
  #{
  #  "api_name": "2-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"<notificationId>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "startnotificationId":"notificationId",
  #    },
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},

  ## 3-1. Empty Pagination.  Status: Done
  #{
  #  "api_name": "3-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":""
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},
  #
  ## 4-1. Invalid Pagination.  Returns 19 rows, where none expected.  Could be a bug.  Status: Done
  #{
  #  "api_name": "4-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"invalid"
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  },
  #  "output_mode": 'n',
  #},

  ## 5-1. Dependent on 1-1 and 2-1. Pagination with valid start and end notifications ids.  Returns 0 rows, while 20 rows are expected.  Could be a bug.  Status: Done
  #{
  #  "api_name": "5-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"<endnotificationId>",
  #    "startNotificationId":"<startnotificationId>"
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 6-1. Dependent on 1-1 and 2-1. Pagination.  Status: Done
  #{
  #  "api_name": "6-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"<endnotificationId>",
  #    "startNotificationId":""
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 7-1. Dependent on 1-1 and 2-1. Pagination.  Returns 0 rows, while 20 rows are expected.  Could be a bug.  Status: Done
  #{
  #  "api_name": "7-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"",
  #    "startNotificationId":"<startnotificationId>"
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 8-1. Dependent on 1-1 and 2-1. Pagination.  Status: Done
  #{
  #  "api_name": "8-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"",
  #    "startNotificationId":""
  #  },
  # "api_expected":{
  #    "rowcount":2,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 9-1. Dependent on 1-1 and 2-1. Invalid Pagination.  Status: Done
  #{
  #  "api_name": "9-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"<endnotificationId>",
  #    "startNotificationId":"abcd"
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 10-1. Dependent on 1-1 and 2-1. Invalid Pagination.  Status: Done
  #{
  #  "api_name": "10-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"abcd",
  #    "startNotificationId":"<startnotificationId>"
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 11-1. Invalid Pagination.  Status: Done
  #{
  #  "api_name": "11-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"",
  #    "startNotificationId":"abcd"
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},
  #
  ## 12-1. Invalid Pagination.  0 rows expected, but 19 returned.  Could be a bug.  Status: Done
  #{
  #  "api_name": "12-getNotifications",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/user/getNotifications",
  #  "api_function": "getNotifications",
  #  "api_params": {
  #    "endNotificationId":"abcd",
  #    "startNotificationId":""
  #  },
  # "api_expected":{
  #    "rowcount":0,
  #    "userId": "<userId>",
  #    "specific":False
  #  }
  #},

]