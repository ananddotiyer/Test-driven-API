#!/usr/bin/env python

#############################################################################################################################################
"""api_object.py: api_object represents the api under test."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from modules.tests.tests_suite import *

class api_object(dict):
	__getattr__= dict.__getitem__
	__setattr__= dict.__setitem__
	
	def __init__(self, test):
		self.api_name = test["api_name"]
		self.api_type = test["api_type"]
		self.api_url = global_dict["server"] + test["api_base_url"]
		self.api_function = test["api_function"]
		self.api_params = test["api_params"]
		
		try:
			self.api_repl = test["api_repl"]
		except:
			self.api_repl = ""
		
		try:
			self.api_headers = test["api_headers"]
		except:
			self.api_headers = ""

		self.api_expected = test["api_expected"]
		try:
			self.api_expected["should_fail"] = test["api_expected"]["should_fail"]
		except:
			self.api_expected["should_fail"] = False #default
			
		try:
			self.output_mode = test["output_mode"]
		except:
			self.output_mode = 'w'	#default

		try:
			self.api_store = test["api_store"]
		except:
			self.api_store = ""
			
		self.actuals_folder = "" #will be filled in from main script
		self.data = "" #will be filled in from main script
		self.status_code = "" #will be filled in from main script