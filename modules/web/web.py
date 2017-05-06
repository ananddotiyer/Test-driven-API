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

from flask import Flask, session, escape, request, send_from_directory, render_template, redirect, url_for, jsonify
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import Required, Length
from werkzeug.utils import secure_filename
from uuid import getnode as get_mac
import traceback
from support import *

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
    if 'username' in session and not escape(session['username']) == "":
        info = logged_in_user (session)
        return render_template('user.html', info=info)
    else:
        return redirect(url_for('login'))    

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if request.method == 'POST':
        session['username'] = form.username.data
        return redirect(url_for('tests'))

    # mac = '-'.join(("%012X" % get_mac())[i:i+2] for i in range(0, 12, 2))
    # form.username.data = '%s' %(mac[:-3])
    return render_template ('login.html', form=form)

    # return '''
    #     <form action="" method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #     </form>
    # '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/tests', methods=('GET', 'POST'))
def tests():
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    test_list = []

    global_dict = main_config (True, escape(session['username']))

    for test in global_dict["tests"]:
        test_list.append (test[0]) #global_dict["tests"] is a tuple consisting of tests, test_category and subfolder

    if request.method == "POST":
        run_selected = []
        check_list = request.form.getlist("select")
        
        for each_test in global_dict["tests"]:
            test = each_test[0] #each_test is a tuple of test, test_category, subfolder.
            cat = each_test[1]
            subfolder = each_test[2]
            
            for check in check_list:
                check = check.split (',')
                if cat == check[0] and test["api_name"] == check[1]:
                    run_selected.append (each_test)
                    break

        global_dict["run_selected"] = run_selected
        
        if not global_dict["running"]:
            global_dict["running"] = True #so that you don't run it again!
            main_driver (True, escape(session['username']))
        
        global_dict["running"] = False #so that you can run it again!
        return redirect(url_for('results'))
    
    return render_template('tests.html', tests=test_list)

@app.route ("/results")
def results ():
    import csv
    import os

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))
    
    try:
        tests_folder = global_dict["test_folder"]
        reader = csv.DictReader(open(tests_folder + 'passfaillog.csv'))

        results_list = []
        for line in reader:
            results_list.append(line)
            
            #making the path for the exported csv file
            file_path = extract_filename_from_hyperlink (line["test_path"])
            
            folder_parts = file_path.split ('\\')
            folder = tests_folder + '\\'.join (folder_parts[:-1]) #tests folder
            filename = folder_parts[-1] #only the filename
            line["test_path"] = "download?folder=%s/&filename=%s" %(folder, filename)
            
            file_path = extract_filename_from_hyperlink (line["result"])
            folder_parts = file_path.split ('\\')
            filename = folder_parts[-1] #only the filename
            line["debuglog"] = "debuglog?debuglog=%s" %(filename)
            line["result"] = extract_text_from_hyperlink (line["result"]) #FAIL, PASS

            file_path = extract_filename_from_hyperlink (line["schema"])
            folder_parts = file_path.split ('\\')
            filename = folder_parts[-1] #only the filename
            schema_file = global_dict["schema_folder"] + filename
            if not os.path.isfile(schema_file):
                line["schema"] = "none"
            line["schema"] = "schema?schema=%s" %(filename)
        return render_template ('results.html', results=results_list)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/run")
def run ():
    import csv
    import os

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))
    
    try:
        # if not global_dict["running"]:
        #     global_dict["running"] = True #so that you don't run it again!
        #     main_driver (True)

        global_dict["running"] = False

        tests_folder = global_dict["test_folder"]
        reader = csv.DictReader(open(tests_folder + 'passfaillog.csv'))

        results_list = []
        for line in reader:
            results_list.append(line)
            
            #making the path for the exported csv file
            file_path = extract_filename_from_hyperlink (line["test_path"])
            folder_parts = file_path.split ('\\')
            folder = tests_folder + '\\'.join (folder_parts[:-1]) #tests folder
            filename = folder_parts[-1] #only the filename
            line["test_path"] = "download?folder=%s&filename=%s" %(folder, filename)
            
            #making the path for the specific debuglog
            file_path = extract_filename_from_hyperlink (line["result"])
            folder_parts = file_path.split ('\\')
            filename = folder_parts[-1] #only the filename
            line["debuglog"] = "debuglog?debuglog=%s" %(filename)
            line["result"] = extract_text_from_hyperlink (line["result"]) #FAIL, PASS

            #making the path for the schema compare file
            file_path = extract_filename_from_hyperlink (line["schema"])
            folder_parts = file_path.split ('\\')
            filename = folder_parts[-1] #only the filename
            schema_file = global_dict["schema_folder"] + filename
            if not os.path.isfile(schema_file):
                line["schema"] = "none"
            line["schema"] = "schema?schema=%s" %(filename)
             
        return render_template ('run.html', results=results_list)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/run_ci")
def run_ci ():
    import csv
    import json

    try:
        username = request.args.get ('username')
    
        global_dict = main_config (True, username=username)
        global_dict["run_selected"] = global_dict["tests"]
    
        main_driver (True, username=username)
    
        tests_folder = global_dict["test_folder"].replace ('\\', '/')
        print tests_folder
        
        line = {"report":"http://localhost:5000/download?folder=%s&filename=passfaillog.csv" %(tests_folder)}
       
        line = json.dumps (line)
        return line
    except:
        return render_template ('no_ops.html')

@app.route ("/schema")
def schema ():
    lines = []
    tabs = []

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    filename = request.args.get ('schema')
    try:
        if not filename:
            reader = open(global_dict["schema_folder"] + "/schema.txt")
        else:
            reader = open(global_dict["schema_folder"] + "/" + filename)
        
        for line in reader:
            tabs_num = (len(line) - len(line.lstrip(' '))) / 4 #number of tabs
            tabs.append (tabs_num)
            lines.append(line.strip ())
        reader.close()
    
        return render_template ('schema.html', indices=range (len (tabs)), tabs=tabs, schema=lines)
    except:
        return render_template ('no_schema.html')

@app.route ("/cleanup")
def cleanup ():
    import os
    import shutil
    
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))
    
    try:
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
    except:
        return render_template ('no_ops.html')

@app.route ("/debuglog")
def debuglog ():
    lines = []

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

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
    
    submit = SubmitField('Duplicate')

class UploadTest (FlaskForm):
    import_from_postman = FileField ()
    upload_tests = FileField ()

    submit = SubmitField('Upload')

class LoginForm (FlaskForm):
    username =  StringField('User name')
    #password =  StringField('Password')

    submit = SubmitField('Login')

@app.route ("/test_upload", methods=('GET', 'POST'))
def test_upload ():
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    try:
        form = UploadTest()

        import_result = ""
        upload_result = ""

        if form.validate_on_submit():
            tests_folder = global_dict["test_folder"] + "Misc"
            #Import POSTMAN tests (exported from POSTMAN)   
            f = form.import_from_postman.data
            if not f.filename == "":
                filename = secure_filename(f.filename)
                f.save(tests_folder + "\\" + filename)
                import_result = import_from_postman (tests_folder, filename, "tests_user_defined")
                if import_result:
                    import_result = "Successfully imported %s into 'Misc' test category" %(filename)
                else:
                    import_result = ""
            
            #Upload the exported file
            f = form.upload_tests.data
            if not f.filename == "":
                filename = secure_filename(f.filename)
                try:
                    f.save(tests_folder + "\\" + filename)
                    upload_result = True
                except:
                    upload_result = False

                if upload_result:
                    upload_result = "Successfully uploaded %s to the server" %(filename)
                else:
                    upload_result = ""
            
            return redirect(url_for('test_uploaded', import_result=import_result, upload_result=upload_result))

        return render_template ('test_upload.html', form=form)
    except:
        traceback.print_exc ()
        #return render_template ('no_test.html')
        return redirect(url_for('test_uploaded', import_result=import_result, upload=upload_result))

@app.route ("/test_created_upload", methods=('GET', 'POST'))
def test_created_upload ():
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    try:
        form = UploadTest()

        if request.method == 'GET':
            form.upload.data = '"tests_user_defined.py"'

        if form.validate_on_submit():
            #Upload the exported file
            tests_folder = global_dict["test_folder"] + "Misc"
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

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))
    tests = global_dict["tests"]

    api_category = request.args.get ('cat')
    api_name = request.args.get ('name')
    
    for each_test in tests:
        test = each_test[0]
        cat = each_test[1]
        subfolder = each_test[2]
        
        if cat == api_category and test["api_name"] == api_name:
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

            mod = import_module (global_dict["test_module"] + "Misc.tests_user_defined")
            tests = getattr (mod, "tests_user_defined")
            
            tests_folder = global_dict["test_folder"] + "Misc/"
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

            return redirect(url_for('test_created')) #creates test (tests_user_defined.py) in tests folder in server.
        return render_template ('duplicate.html', form=form)
    except:
        traceback.print_exc ()
        return render_template ('no_results.html', running=global_dict["running"])

@app.route ("/delete", methods=('GET','POST'))
def delete ():
    lines = []

    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))
    tests = global_dict["tests"]

    api_category = request.args.get ('cat')
    api_name = request.args.get ('name')
    
    for each_test in tests:
        test = each_test[0] #each_test is a tuple of test, test_category, subfolder.
        cat = each_test[1]
        subfolder = each_test[2]

        if cat == api_category and test["api_name"] == api_name:
            break
    try:
        mod = import_module (global_dict["test_module"] + "Misc.tests_user_defined")
        tests = getattr (mod, "tests_user_defined")
        tests.remove (test)
        
        tests_folder = global_dict["test_folder"] + "Misc/"
        with open (tests_folder + "tests_user_defined.py", "w") as fp:
            fp.write ("tests_user_defined = [\n")
            #existing tests
            for test in tests:
                fp.write ("{\n")
                for each in test:
                    print test[each], type (test[each] )
                    if type (test[each] ) == str or type (test[each] ) == unicode:
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
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    folder = request.args.get ('folder')
    filename = request.args.get ('filename')
    
    if "tests_%s" %(escape(session['username'])) in folder: #allow only tests for the corresponding login to be downloaded
        return send_from_directory(folder, filename, as_attachment=True)
    else:
        return render_template ('no_test.html')

@app.route ("/test_uploaded")
def test_uploaded ():
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    return render_template ('test_uploaded.html',import_result=request.args.get ("import_result"), upload_result=request.args.get ("upload_result"))

@app.route ("/test_created")
def test_created ():
    if not 'username' in session:
        info = logged_in_user (session)
        return render_template('user.html', info=info)

    global_dict = main_config (True, escape(session['username']))

    return render_template ('test_created.html')

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    # set the secret key.  keep this really secret:
    #app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    while True:
        print "Restarting..."
        app.run(host='0.0.0.0', threaded=True, debug=True)