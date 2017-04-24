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

from flask import Flask, request, send_from_directory, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import Required, Length
from werkzeug.utils import secure_filename
import traceback

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top secret!'
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

    tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests"

    for tests in tests_suite:
        tests_in_folder = tests.split ('.')
    
        #import only the required list of tests; contained in test_list
        mod = import_module ("tests." + tests)
        
        additional_tests = getattr (mod, tests_in_folder[-1])
        test_list.extend (additional_tests)
        for test in additional_tests:
            test["api_category"] = '.'.join (tests_in_folder[-2:])
            folder_parts = (tests_folder + "\\" + test["api_category"]).replace ('.','\\').split ('\\')
            folder = '\\'.join (folder_parts[:-1]) #tests folder
            filename = folder_parts[-1] + ".py" #only the filename.
            test["api_download"] = "download?folder=%s&filename=%s" %(folder, filename) #download tests

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
            
            folder_parts = line["test_path"].split ('\\')
            folder = tests_folder + '\\' + '\\'.join (folder_parts[:-1]) #tests folder
            filename = folder_parts[-1] #only the filename
            line["test_path"] = "download?folder=%s&filename=%s" %(folder, filename)
            
            #making the path for the specific debuglog
            split_result = line["result"].replace ('=HYPERLINK', "").split (',')
            line["debuglog"] = split_result[0].strip ('"()\\') #new field contains filename.
            line["debuglog"] = "debuglog?debuglog=%s" %(line["debuglog"])
            line["result"] = split_result[1].strip ('"()\\') #FAIL, PASS

            #making the path for the schema compare file
            line["schema"] = line["schema"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["schema"] = "schema?schema=%s" %(line["schema"])
             
        return render_template ('results.html', results=results_list)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/run")
def run ():
    import csv
    import os

    global_dict = main_config (True)
    
    try:
        if not global_dict["running"]:
            global_dict["running"] = True #so that you don't run it again!
            main_driver (True)

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

            folder_parts = line["test_path"].split ('\\')
            folder = tests_folder + '\\' + '\\'.join (folder_parts[:-1]) #tests folder
            filename = folder_parts[-1] #only the filename
            line["test_path"] = "download?folder=%s&filename=%s" %(folder, filename)
            
            #making the path for the specific debuglog
            split_result = line["result"].replace ('=HYPERLINK', "").split (',')
            line["debuglog"] = split_result[0].strip ('"()\\') #new field contains filename.
            line["debuglog"] = "debuglog?debuglog=%s" %(line["debuglog"])
            line["result"] = split_result[1].strip ('"()\\') #FAIL, PASS

            #making the path for the schema compare file
            line["schema"] = line["schema"].replace ('=HYPERLINK', "").split (',')[0].strip ('"()\\')
            line["schema"] = "schema?schema=%s" %(line["schema"])
             
        return render_template ('run.html', results=results_list)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/schema")
def schema ():
    lines = []
    tabs = []

    global_dict = main_config (True)

    filename = request.args.get ('schema')
    if not filename:
        reader = open('..\\tests\\schema.txt')
    else:
        reader = open(global_dict["schema_folder"] + "/" + filename)
    
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

@app.route ("/debuglog")
def debuglog ():
    lines = []

    global_dict = main_config (True)

    filename = request.args.get ('debuglog')
    reader = open(global_dict["debuglog"] + "/" + filename)
    for line in reader:
        lines.append(line.strip ())
    reader.close()

    try:
        return render_template ('debuglog.html', lines=lines)
    except:
        return render_template ('no_results.html', running=global_dict["running"])

class CreateNewTest (FlaskForm):
    name = StringField('Name: ', validators=[Required(), Length(1, 30)])
    method = StringField('Type: ')
    url = StringField('URL: ', validators=[Required(), Length(1, 1000)], render_kw={"style":"width: 1000px;"})
    parameters = StringField('Parameters: ', render_kw={"style":"width: 1000px;"})
    expected = StringField('Expected: ', validators=[Required()], render_kw={"style":"width: 1000px;"})
    repl = StringField('Replace string: ')
    store = StringField('Store: ')
    function = StringField('Function: ', validators=[Required()])
    output = StringField('Output mode: ', validators=[Required(), Length(1, 3)])
    #upload = FileField ()
    
    submit = SubmitField('Submit')

class UploadTest (FlaskForm):
    upload = FileField ()

    submit = SubmitField('Submit')

@app.route ("/test_upload", methods=('GET', 'POST'))
def test_upload ():
    global_dict = main_config (True)

    try:
        form = UploadTest()

        if form.validate_on_submit():
            #Upload the exported file
            tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests/Misc"
            f = form.upload.data
            filename = secure_filename(f.filename)
            f.save(tests_folder + "\\" + filename)

            return redirect(url_for('test_uploaded'))

        return render_template ('test_upload.html', form=form)
    except:
        traceback.print_exc ()
        return render_template ('no_test.html')

@app.route ("/test_created_upload", methods=('GET', 'POST'))
def test_created_upload ():
    global_dict = main_config (True)

    try:
        form = UploadTest()

        if request.method == 'GET':
            form.upload.data = '"tests_user_defined.py"'

        if form.validate_on_submit():
            #Upload the exported file
            tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests/Misc"
            f = form.upload.data
            filename = secure_filename(f.filename)
            f.save(tests_folder + "\\" + filename)

            return redirect(url_for('test_uploaded'))

        return render_template ('test_upload.html', form=form)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/duplicate", methods=('GET', 'POST'))
def duplicate ():
    lines = []

    global_dict = main_config (True)
    tests = global_dict["tests"]

    api_category = request.args.get ('cat')
    api_name = request.args.get ('name')
    
    for each_test in tests:
        test = each_test[0]
        cat = each_test[1]
        subfolder = each_test[2]
        if "%s.%s" %(subfolder, cat) == api_category and test["api_name"] == api_name:
            break
    try:
        form = CreateNewTest()
        
        #Pre-populate data
        if request.method == 'GET':
            form.name.data = '"%s"' %(test["api_name"])
            form.method.data = '"%s"' %(test["api_type"])
            form.url.data = '"%s"' %(test["api_url"])
            form.parameters.data = test["api_params"]
            form.expected.data = test["api_expected"]
            form.repl.data = test["api_repl"]
            form.store.data = test["api_store"]
            form.function.data = '"%s"' %(test["api_function"])
            form.output.data = '"%s"' %(test["output_mode"])
        
        new_test = {}
        if form.validate_on_submit():
            new_test["api_name"] = form.name.data
            new_test["api_type"] = form.method.data
            new_test["api_url"] = form.url.data
            new_test["api_params"] = form.parameters.data
            new_test["api_expected"] = form.expected.data
            new_test["api_repl"] = form.repl.data
            new_test["api_store"] = form.store.data
            new_test["api_function"] = form.function.data
            new_test["output_mode"] = form.output.data

            mod = import_module ("modules.tests.Misc.tests_user_defined")
            tests = getattr (mod, "tests_user_defined")
            
            tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests/Misc/"
            with open (tests_folder + "tests_user_defined.py", "w") as fp:
                fp.write ("tests_user_defined = [\n")
                #existing tests
                for test in tests:
                    fp.write ("{\n")
                    for each in test:
                        if not type (test[each] ) == dict or type (test[each] ) == list:
                            fp.write ('\t"%s" : "%s",\n' %(each, test[each]))
                        else:
                            fp.write ('\t"%s" : %s,\n' %(each, test[each]))
                            
                    fp.write ("},\n")
                
                #new test
                fp.write ("{\n")
                for each in new_test:
                    fp.write ('\t"%s" : %s,\n' %(each, new_test[each]))
                fp.write ("}\n")
                fp.write ("]")

            #return redirect(url_for('test_created_upload')) #this form creates test (tests_user_defined.py) locally.  Also allows to select file and upload it to tests folder in server.
            return redirect(url_for('test_created')) #creates test (tests_user_defined.py) in tests folder in server.
        return render_template ('duplicate.html', form=form)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/delete", methods=('GET','POST'))
def delete ():
    lines = []

    global_dict = main_config (True)
    tests = global_dict["tests"]

    api_category = request.args.get ('cat')
    api_name = request.args.get ('name')
    
    for each_test in tests:
        test = each_test[0] #each_test is a tuple of test, test_category, subfolder.
        cat = each_test[1]
        subfolder = each_test[2]
        if "%s.%s" %(subfolder, cat) == api_category and test["api_name"] == api_name:
            break
    try:
        mod = import_module ("modules.tests.Misc.tests_user_defined")
        tests = getattr (mod, "tests_user_defined")
        tests.remove (test)
        
        tests_folder = path.dirname(path.dirname(path.dirname(path.abspath(__file__)))) + "/modules/tests/Misc/"
        with open (tests_folder + "tests_user_defined.py", "w") as fp:
            fp.write ("tests_user_defined = [\n")
            #existing tests
            for test in tests:
                fp.write ("{\n")
                for each in test:
                    if type (test[each] ) == str:
                        fp.write ('\t"%s" : "%s",\n' %(each, test[each]))
                    else:
                        fp.write ('\t"%s" : %s,\n' %(each, test[each]))
                        
                fp.write ("},\n")
            fp.write ("]")
                
        return render_template ('test_deleted.html') #deletes test (tests_user_defined.py) from  tests folder in server.
    except:
        traceback.print_exc ()
        return render_template ('no_test.html')

@app.route ("/download")
def download ():
    global_dict = main_config (True)

    folder = request.args.get ('folder')
    filename = request.args.get ('filename')
    
    if "tests" in folder: #allow only tests to be downloaded
        return send_from_directory(folder, filename, as_attachment=True)
    else:
        return render_template ('no_test.html')

@app.route ("/test_uploaded")
def test_uploaded ():
    global_dict = main_config (True)

    return render_template ('test_uploaded.html')

@app.route ("/test_created")
def test_created ():
    global_dict = main_config (True)

    return render_template ('test_created.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)