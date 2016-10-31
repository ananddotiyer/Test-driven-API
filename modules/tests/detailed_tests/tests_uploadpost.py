#!/usr/bin/env python

#############################################################################################################################################
"""tests_uploadpost.py: Upload post tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_uploadpost = [
  ################################################Pre-conditions-getVerificationCode,getAccessToken########################################################
  # P-1. Status: Done
  {
    "api_name": "P-1-getVerificationCode",
    "api_type": "POST",
    "api_base_url": "/api/v1/user/getVerificationCode",
    "api_function": "getVerificationCode",
    "api_params": {
      "phone": "+919845177582"
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
        "phone": "+919845177582",
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

  ################################################uploadLifePost, getLifePost########################################################
  ## 1-1. Status: Done
  #{
  #  "api_name": "1-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Text post-1"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  # 1-2. Status: Done
  #{
  #  "api_name": "1-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},  

  ## 2-1. Blank text. Status: Done
  #{
  #  "api_name": "2-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": ""
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  # 2-2. Status: Done
  #{
  #  "api_name": "2-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},  

  #
  ## 3-1. Text lengthier than 160 characters. Status: Done
  #{
  #  "api_name": "3-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"textLimitExceeded",
  #    "message":"With words, less is more. Limit: 160 chars for text-only post, 60 chars for all other text.",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 4-1. Text with hash tag. Status: Done
  #{
  #  "api_name": "4-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Text #post-2"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 4-2. Status: Done
  #{
  #  "api_name": "4-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},  
  #
  ## 5-1. Text with only hash tag. Status: Done
  #{
  #  "api_name": "5-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "#post"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 5-2. Status: Done
  #{
  #  "api_name": "5-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},  

  ## 6-1. Audio. Status: Done
  #{
  #  "api_name": "5-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 2,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 6-2. Status: Done
  #{
  #  "api_name": "6-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postAudio":"http://www.example.com/url/to/audio.m4a",
  #    "specific":False
  #  }
  #},  
  #
  ## 7-1. Status: Done
  #{
  #  "api_name": "7-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Text post-2"
  #  },
  #  "api_store": {
  #    "response": {
  #      "originalPostId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 7-2. Share the previous post. Status: Done
  #{
  #  "api_name": "7-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 3,
  #    "postId": "<originalPostId>"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 7-3. Status: Done
  #{
  #  "api_name": "7-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "originalPostId\postId":"<originalPostId>",
  #    "specific":False
  #  }
  #},  
  #
  ## 8-1. Upload image post. Status: Done
  #{
  #  "api_name": "8-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 4,
  #    "postImage": "http://www.example.com/url/to/image.jpg"
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 8-2. Status: Done
  #{
  #  "api_name": "8-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postImage":"http://www.example.com/url/to/image.jpg",
  #    "specific":False
  #  }
  #},  
  #
  ## 9-1. Upload voxPic post. Status: Done
  #{
  #  "api_name": "9-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 5,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postAudio":"http://www.example.com/url/to/audio.m4a",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 9-2. Status: Done
  #{
  #  "api_name": "9-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postImage":"http://www.example.com/url/to/image.jpg",
  #    "postAudio":"http://www.example.com/url/to/audio.m4a",
  #    "specific":False
  #  }
  #},  
  #
  ## 10-1. Upload smiley post. Status: Done
  #{
  #  "api_name": "10-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 6,
  #    "postText": "smiley face text",
  #    "postSmiley": "smiley face",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 10-2. Status: Done
  #{
  #  "api_name": "10-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postText": "smiley face text",
  #    "postSmiley": "smiley face",
  #    "specific":False
  #  }
  #},  
  #
  ## 11-1. Upload voxsmiley post. Status: Done
  #{
  #  "api_name": "11-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 7,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postSmiley": "smiley face",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 11-2. Status: Done
  #{
  #  "api_name": "11-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postSmiley": "smiley face",
  #    "specific":False
  #  }
  #},  
  #
  ## 11-1. Upload voxsmiley post. Status: Done
  #{
  #  "api_name": "12-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 8,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postText": "voxText-1",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 12-2. Status: Done
  #{
  #  "api_name": "12-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postText": "voxText-1",
  #    "specific":False
  #  }
  #},  
  #
  ## 13-1. Text lengthier than 160 characters in a voxText. Status: Done
  #{
  #  "api_name": "13-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 8,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postText": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"textLimitExceeded",
  #    "message":"With words, less is more. Limit: 160 chars for text-only post, 60 chars for all other text.",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 14-1. Upload imageText post. Status: Done
  #{
  #  "api_name": "14-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 9,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "imageText-1",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 14-2. Status: Done
  #{
  #  "api_name": "14-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "imageText-1",
  #    "specific":False
  #  }
  #},  
  #
  ## 15-1. Text lengthier than 160 characters in a imageText. Status: Done
  #{
  #  "api_name": "15-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 9,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"textLimitExceeded",
  #    "message":"With words, less is more. Limit: 160 chars for text-only post, 60 chars for all other text.",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 16-1. Upload video post. Status: Done
  #{
  #  "api_name": "16-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 10,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 16-2. Status: Done
  #{
  #  "api_name": "16-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #    "specific":False
  #  }
  #},  
  #
  ## 17-1. Upload videoText post. Status: Done
  #{
  #  "api_name": "17-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 11,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #    "postText": "videoText-1",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 17-2. Status: Done
  #{
  #  "api_name": "17-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #    "postText": "videoText-1",
  #    "specific":False
  #  }
  #},  
  #
  ## 18-1. Text lengthier than 160 characters in a videoText. Status: Done
  #{
  #  "api_name": "18-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 11,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #    "postText": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"textLimitExceeded",
  #    "message":"With words, less is more. Limit: 160 chars for text-only post, 60 chars for all other text.",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 19-1. Upload voxPicText post. Status: Done
  #{
  #  "api_name": "19-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 12,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #   "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "videoText-1",
  #  },
  #  "api_store": {
  #    "response": {
  #      "postId":"postId",
  #    },
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post successfully created!",
  #    "specific":False
  #  }
  #},
  ## 19-2. Status: Done
  #{
  #  "api_name": "19-getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": "<postId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "videoText-1",
  #    "specific":False
  #  }
  #},  
  #
  ## 20-1. Text lengthier than 160 characters in a voxPicText. Status: Done
  #{
  #  "api_name": "20-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 12,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "abcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghijabcdefghija"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"textLimitExceeded",
  #    "message":"With words, less is more. Limit: 160 chars for text-only post, 60 chars for all other text.",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 21-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "21-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 2,
  #    "postText": "Text post-1"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 2, postAudio is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 22-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "22-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 1, postText is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 23-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "23-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 4,
  #    "postId": "<originalPostId>"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 4, postImage is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 24-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "24-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 3,
  #    "postImage": "http://www.example.com/url/to/image.jpg"
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 3, postId is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 25-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "25-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 6,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postAudio":"http://www.example.com/url/to/audio.m4a",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 6, postText is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 26-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "26-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 5,
  #    "postText": "smiley face text",
  #    "postSmiley": "smiley face",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 5, postImage is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 27-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "27-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 8,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postSmiley": "smiley face",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 8, postText is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 28-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "28-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 7,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postText": "voxText-1",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 7, postSmiley is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 29-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "29-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 10,
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "imageText-1",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 10, postVideo is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 30-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "30-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 9,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 9, postText is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 31-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "31-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 12,
  #    "postVideo": "http://www.example.com/url/to/video.mp4",
  #    "postText": "videoText-1",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 12, postImage is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},
  #
  ## 32-1. Wrong postType.  Status: Done
  #{
  #  "api_name": "32-uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 11,
  #    "postAudio": "http://www.example.com/url/to/audio.m4a",
  #    "postImage": "http://www.example.com/url/to/image.jpg",
  #    "postText": "videoText-1",
  #  },
  #  "api_expected":{
  #    "rowcount":0,
  #    "errorCode":"syntaxError",
  #    "message":"For postType = 11, postVideo is a mandatory field",
  #    "specific":False,
  #    "should_fail":True
  #  }
  #},

]