tests_hashtag = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500009"
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
        "phone": "+919876500009",
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

  ################################################getHashtagPage########################################################
  
  #  ## 1-1. . Status: Done.
  #  {
  #    "api_name": "1-getHashtagPage",
  #    "api_type": "POST",
  #    "api_base_url": "/api/v1/life/getHashtagPage",
  #    "api_function": "getHashtagPage",
  #    "api_params": {
  #      "hashtag": "#automationframework"
  #      },
  #    "api_store": {
  #      "response": {
  #        "content\postId":"postId",
  #        },
  #    },
  #    "api_expected":{
  #      "rowcount":20,
  #      "specific":False,
  #      },
  #    
  #  },
  #  
  ### 1-2. Pagination . Status: Done.
  #{
  #  "api_name": "1-2-getHashtagPage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getHashtagPage",
  #  "api_function": "getHashtagPage",
  #  "api_params": {
  #    "hashtag": "#automationframework",
  #    "endId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":2,
  #    "specific":False,
  #  },
  #},
  #      
  ### 2-1. Blank Hash . Status: Done.
  #{
  #  "api_name": "2-getHashtagPage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getHashtagPage",
  #  "api_function": "getHashtagPage",
  #  "api_params": {
  #    "hashtag": "",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #  },
  #},
  #
  ### 3-1. Invalid Pagination . Status: Done. Bug Fix Needed.
  #{
  #  "api_name": "3-getHashtagPage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getHashtagPage",
  #  "api_function": "getHashtagPage",
  #  "api_params": {
  #    "hashtag": "#automationframework",
  #    "endId": "SomeRandomKeystrokes"  
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #  },
  #},
  #
  ### 4-1. Blank Pagination . Status: Done.
  #{
  #  "api_name": "4-getHashtagPage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getHashtagPage",
  #  "api_function": "getHashtagPage",
  #  "api_params": {
  #    "hashtag": "#automationframework",
  #    "endId": ""
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "specific":False,
  #  },
  #},  
]