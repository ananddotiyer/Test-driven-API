from importlib import import_module

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)
bootstrap = Bootstrap(app)

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

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
        
        print test_list
        
    return render_template('index.html', server=global_dict["server"], tests=test_list)

@app.route ("/run")
def run ():
    import csv
    reader = csv.DictReader(open('..\\tests\\passfaillog.csv'))
    results_list = []
    for line in reader:
        results_list.append(line)

    return render_template ('run.html', results=results_list)

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(debug=True)
