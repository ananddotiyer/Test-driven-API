#############################################################################################################################################
"""web.py: This is the web server.  Keep this running"""

__author__ = "Anand Iyer"
__copyright__ = "Copyright 2016-17, Anand Iyer"
__credits__ = ["Anand Iyer"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Anand Iyer"
__email__ = "ananddotiyer@gmail.com"
__status__ = "Production"
#############################################################################################################################################

from importlib import import_module

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))

from main import main_config, main_driver
from tests.tests_suite import *
    
@app.route('/')
def index():
    test_list = []

    global_dict = main_config (True)

    for tests in tests_suite:
        tests_in_folder = tests.split ('.')
    
        #import only the required list of tests; contained in test_list
        mod = import_module ("tests." + tests)
        
        additional_tests = getattr (mod, tests_in_folder[-1])
        test_list.extend (additional_tests)
        for test in additional_tests:
            test["api_category"] = tests_in_folder[-1]

    return render_template('index.html', tests=test_list)

@app.route ("/results")
def results ():
    import csv
    import os

    global_dict = main_config (True)
    
    try:
        reader = csv.DictReader(open('..\\tests\\passfaillog.csv'))

        tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests"
        debuglog_folder = tests_folder + "/debuglog"
        schema_folder = tests_folder + "/schema"

        results_list = []
        for line in reader:
            results_list.append(line)
            
            #making the path for the exported csv file
            line["test_path"] = line["test_path"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["test_path"] = "file://%s/%s" %(tests_folder,line["test_path"])
            
            #making the path for the specific debuglog
            split_result = line["result"].replace ('=HYPERLINK', "").split (',')
            line["debuglog"] = split_result[0].strip ('"()\\') #new field contains filename.
            line["debuglog"] = "file://%s/%s" %(debuglog_folder,line["debuglog"])
            line["result"] = split_result[1].strip ('"()\\') #FAIL, PASS

            #making the path for the schema compare file
            line["schema"] = line["schema"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["schema"] = "file://%s/%s" %(schema_folder,line["schema"])
             
        return render_template ('results.html', results=results_list)
    except:
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/run")
def run ():
    import csv
    import os

    global_dict = main_config (True)
    
    try:
        if not global_dict["running"]:
            global_dict["running"] = True #so that you don't run it again!
            main_driver ()
        
        reader = csv.DictReader(open('..\\tests\\passfaillog.csv'))
        global_dict["running"] = False

        tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests"
        debuglog_folder = tests_folder + "/debuglog"
        schema_folder = tests_folder + "/schema"

        results_list = []
        for line in reader:
            results_list.append(line)
            
            #making the path for the exported csv file
            line["test_path"] = line["test_path"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["test_path"] = "file://%s/%s" %(tests_folder,line["test_path"])
            
            #making the path for the specific debuglog
            split_result = line["result"].replace ('=HYPERLINK', "").split (',')
            line["debuglog"] = split_result[0].strip ('"()\\') #new field contains filename.
            line["debuglog"] = "file://%s/%s" %(debuglog_folder,line["debuglog"])
            line["result"] = split_result[1].strip ('"()\\') #FAIL, PASS

            #making the path for the schema compare file
            line["schema"] = line["schema"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["schema"] = "file://%s/%s" %(schema_folder,line["schema"])
             
        return render_template ('run.html', results=results_list)
    except:
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/schema")
def schema ():
    lines = []
    tabs = []

    global_dict = main_config (True)

    reader = open('..\\tests\\schema.txt')
    for line in reader:
        tabs_num = (len(line) - len(line.lstrip(' '))) / 4 #number of tabs
        tabs.append (tabs_num)
        lines.append(line.strip ())
    reader.close()

    try:
        return render_template ('schema.html', indices=range (len (tabs)), tabs=tabs, schema=lines)
    except:
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/cleanup")
def cleanup ():
    import os
    import shutil
    
    global_dict = main_config (True)
    
    schema_folder = global_dict["schema_folder"]
    for file in os.listdir(schema_folder):
        if not file == "__init__.py":
            os.remove (schema_folder + "\\" + file)

    debuglog_folder = global_dict["debuglog"]
    for file in os.listdir(debuglog_folder):
        if not file == "__init__.py":
            os.remove (debuglog_folder + "\\" + file)

    shutil.copy (global_dict["test_folder"] + "passfaillog_blank.csv", global_dict["test_folder"] + "passfaillog.csv")

    return render_template ('cleanup.html')
    
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)