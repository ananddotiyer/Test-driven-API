tests_user_defined = [
  {
    "api_name": "1-appkeyhomeslug",
    "api_type": "POST",
    "api_url": "http://dev.media.jio.com/n18/apis/{key}/v3/homeslug/get/1/1/303",
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
      "rowcount":23,
      "call_compare_equals": {
        "$.code": [200],
        "$.['item'][0].['primary_category'][0].['slug']": ["technology"]
      },
      "call_compare_types": {
        "$.code": "int",
        "$.['item'][0].['primary_category'][0].['slug']": "unicode"
      },
      "response_schema": "match",
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