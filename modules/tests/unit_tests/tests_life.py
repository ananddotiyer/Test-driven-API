#!/usr/bin/env python

#############################################################################################################################################
"""tests_life.py: Life tests for vxwb"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2014-15, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

tests_life = [
  ################################################/life########################################################
  ## life/getLifePage.  Status: Done
  #{
  #  "api_name": "getLifePage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePage",
  #  "api_function": "getLifePage",
  #  "api_params": {
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/uploadLifePost.  Status: Done
  #{
  #  "api_name": "uploadLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLifePost",
  #  "api_function": "uploadLifePost",
  #  "api_params": {
  #    "postType": 1,
  #    "postText": "Here is the third post from Anand #Api"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/getLifePost.  Status: Done
  #{
  #  "api_name": "getLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getLifePost",
  #  "api_function": "getLifePost",
  #  "api_params": {
  #    "postId": ["14d2d63d779q.4Y1q4nGcaINx8pc17CDV","14d7ba2ae32R2taqqKbHaX_atQb5gLUMF"]
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/removeVoiceFromVoxPic.  Status: Done
  #{
  #  "api_name": "removeVoiceFromVoxPic",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/removeVoiceFromVoxPic",
  #  "api_function": "removeVoiceFromVoxPic",
  #  "api_params": {
  #    "postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    #"message":"Removed voice from VoxPic!",
  #    "message":"Not found",
  #    "specific":False
  #  }
  #},
  ## life/deleteLifePost.  Status: Done
  #{
  #  "api_name": "deleteLifePost",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLifePost",
  #  "api_function": "deleteLifePost",
  #  "api_params": {
  #    "postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post deleted!",
  #    "specific":False
  #  }
  #},
  ## life/uploadLike.  Status: Done
  #{
  #  "api_name": "uploadLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadLike",
  #  "api_function": "uploadLike",
  #  "api_params": {
  #    "postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV",
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post liked!",
  #    "specific":False
  #  }
  #},
  ## life/deleteLike.  Status: Done
  #{
  #  "api_name": "deleteLike",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/deleteLike",
  #  "api_function": "deleteLike",
  #  "api_params": {
  #    "postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV",
  #    "userId": "<userId>"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Post unliked!",
  #    "specific":False
  #  }
  #},
  ## life/getPostLikes.  Status: Done
  #{
  #  "api_name": "getPostLikes",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostLikes",
  #  "api_function": "getPostLikes",
  #  "api_params": {
  #    "postId": "14d48aceef0q_A1ZoW2HCDesq3CH0NSZk",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/uploadComment.  Status: Done
  #{
  #  "api_name": "uploadComment",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/uploadComment",
  #  "api_function": "uploadComment",
  #  "api_params": {
  #    #"postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV",
  #    #"userId": "184dfb1d521fbb76487139df2e65f33a1431337456009",
  #    "postId": "14d7ba2ae32R2taqqKbHaX_atQb5gLUMF",
  #    "userId": "184dfb1d521fbb76487139df2e65f33a1431337456009",
  #    "commentText": "This is the third #api comment with hash tag!",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"Comment added successfully!",
  #    "specific":False
  #  }
  #},
  ## life/getPostComments.  Status: Done
  #{
  #  "api_name": "getPostComments",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getPostComments",
  #  "api_function": "getPostComments",
  #  "api_params": {
  #    "postId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/getHashtagPage.  Status: Done
  #{
  #  "api_name": "getHashtagPage",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/getHashtagPage",
  #  "api_function": "getHashtagPage",
  #  "api_params": {
  #    "hashtag": "#api"
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "specific":False
  #  }
  #},
  ## life/reportContent.  Status: Done
  #{
  #  "api_name": "reportContent",
  #  "api_type": "POST",
  #  "api_base_url": "/api/v1/life/reportContent",
  #  "api_function": "reportContent",
  #  "api_params": {
  #    "contentType": "1",
  #    "reportType": "0",
  #    "contentId": "14d2d63d779q.4Y1q4nGcaINx8pc17CDV",
  #    "message": "This post infringes my copyright!",
  #  },
  #  "api_expected":{
  #    "rowcount":1,
  #    "message":"A report has been made. We shall look into it.",
  #    "specific":False
  #  }
  #},
]