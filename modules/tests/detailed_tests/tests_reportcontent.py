tests_reportcontent = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919876500000"
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
        "phone": "+919876500000",
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

  ################################################reportContent########################################################
  
    ### 1-1. Positive case. Status: Done.
    #{
    #  "api_name": "1-reportContent",
    #  "api_type": "POST",
    #  "api_base_url": "/api/v1/life/reportContent",
    #  "api_function": "reportContent",
    #  "api_params": {
    #    "contentType": "1",
    #    "reportType": "0",
    #    "contentId": "14db4067633_oSiOq1bFlmRwWCcdje5vF", #Content uploaded by : Automation7 : PostId :14db4067633_oSiOq1bFlmRwWCcdje5vF
    #    "message": "This post infringes my copyright!'",
    #  },
    #  "api_expected":{
    #    "rowcount":1,
    #    "message": "A report has been made. We shall look into it.",
    #    "specific":False,
    #  },
    #},
    #
    ### 2-1. Invalid Postid. Status: Done. Bug Fix required.
    #{
    #  "api_name": "2-reportContent",
    #  "api_type": "POST",
    #  "api_base_url": "/api/v1/life/reportContent",
    #  "api_function": "reportContent",
    #  "api_params": {
    #    "contentType": "2",
    #    "reportType": "2",
    #    "contentId": "SomeRandomKeystrokes",
    #    "message": "This post infringes my copyright!'",
    #  },
    #  "api_expected":{
    #    "rowcount":1,
    #    "should_fail":True,
    #    "message": "postIdInvalid",
    #    "specific":False,
    #  },
    #},
    #
    ### 3-1. Invalid Postid. Status: Done. Bug Fix required.
    #{
    #  "api_name": "3-reportContent",
    #  "api_type": "POST",
    #  "api_base_url": "/api/v1/life/reportContent",
    #  "api_function": "reportContent",
    #  "api_params": {
    #    "contentType": "3",
    #    "reportType": "3",
    #    "contentId": "SomeRandomKeystrokes",
    #    "message": "This post infringes my copyright!'",
    #  },
    #  "api_expected":{
    #    "rowcount":1,
    #    "should_fail":True,
    #    "message": "commentIdInvalid",
    #    "specific":False,
    #  },
    #},
    #
    ### 4-1. Blank Content And Report Type. Status: Done. Bug Fix Required.
    #{
    #  "api_name": "4-reportContent",
    #  "api_type": "POST",
    #  "api_base_url": "/api/v1/life/reportContent",
    #  "api_function": "reportContent",
    #  "api_params": {
    #    "contentType": "",
    #    "reportType": "",
    #    "contentId": "14db4067633_oSiOq1bFlmRwWCcdje5vF",
    #    "message": "This post infringes my copyright!'",
    #  },
    #  "api_expected":{
    #    "rowcount":1,
    #    "message": "reportTypeInvalid",
    #    "should_fail":True,
    #    "specific":False,
    #  },
    #},
    #
    ### 5-1. Invalid Type. Status: Done. Bug Fix Required.
    #{
    #  "api_name": "5-reportContent",
    #  "api_type": "POST",
    #  "api_base_url": "/api/v1/life/reportContent",
    #  "api_function": "reportContent",
    #  "api_params": {
    #    "contentType": "$",
    #    "reportType": "3",
    #    "contentId": "14db4067633_oSiOq1bFlmRwWCcdje5vF",
    #    "message": "This post infringes my copyright!'",
    #  },
    #  "api_expected":{
    #    "rowcount":1,
    #    "message": "Unexpected token $",
    #    "should_fail":True,
    #    "specific":False,
    #  },
    #},
]