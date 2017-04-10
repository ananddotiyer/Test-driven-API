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

from main import main_driver
from tests.tests_suite import *
    
@app.route('/')
def index():
    test_list = []

    for tests in tests_suite:
        tests_in_folder = tests.split ('.')
    
        #import only the required list of tests; contained in test_list
        mod = import_module ("tests." + tests)
        
        additional_tests = getattr (mod, tests_in_folder[-1])
        test_list.extend (additional_tests)
        for test in additional_tests:
            test["api_category"] = tests_in_folder[-1]
        
    return render_template('index.html', server=global_dict["server"], tests=test_list)

@app.route ("/run")
def run ():
    import csv
    import os
    
    try:
        if not global_dict["running"]:
            global_dict["running"] = True #so that you don't run it again!
            main_driver (True)
        
        reader = csv.DictReader(open('..\\tests\\passfaillog.csv'))
        global_dict["running"] = False

        tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests"

        results_list = []
        for line in reader:
            results_list.append(line)
            #making the path for the exported csv file
            line["test_path"] = line["test_path"].replace ('=HYPERLINK', "").split (',')[1].strip ('")\\')
            line["test_path"] = "file://%s/%s.csv" %(tests_folder,line["test_path"])
             
        return render_template ('run.html', results=results_list)
    except:
        return render_template ('no_results.html', running=global_dict["running"])

#Cannot get this to work.  Always raises exception.  When schema.html is rendered without parameters, it works sometimes, but not always.
@app.route ("/schema")
def schema ():
    try:
        lines = []
        tabs = []
        reader = open('..\\tests\\schema.txt')
        for line in reader:
            tabs_num = (len(line) - len(line.lstrip(' '))) / 4 #number of tabs
            tabs.append (tabs_num)
            lines.append(line.strip ())
        reader.close()
        
        num_lines = len (lines)
        
        return render_template ('schema.html', num_lines=num_lines, tabs=tabs, schema=lines)
        #return render_template ('schema.html')
    except:
        return render_template ('no_results.html', running=global_dict["running"])
    
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
