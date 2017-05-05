#############################################################################################################################################
"""sm.py: This is the support functions used by controller."""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################
def _append (variable, tests_folder_name, key, value):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	getattr (mod_main, tests_variable)[key].append (value)

def _set_in_list (variable, tests_folder_name, key, value):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	getattr (mod_main, tests_variable)[key] = value

def _get_in_list (variable, tests_folder_name, key):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	return getattr (mod_main, tests_variable)[key]

def _update_in_list (variable, tests_folder_name, key, value):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	getattr (mod_main, tests_variable)[key].update (value)

def _set (variable, tests_folder_name, value):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	setattr (mod_main, tests_variable, value)

def _get (variable, tests_folder_name):
	mod_main = __import__ (__name__)
	tests_variable = "mod_%s_%s" %(tests_folder_name, variable)
	return getattr (mod_main, tests_variable)