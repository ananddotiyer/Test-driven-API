# Test driven! API

To view web interface, run "python web.py" in command-line, from modules\web path.  Web interface is available at localhost:5000

Features and benefits of Test-driven! include:

* Python-based framework to test web-services, directly at the end-point.
* The main driver is independent of your tests.  Tests themselves are JSON-formatted templates.
* The template is the test script.  To create a new template (test), use the provided default template and start modifying.
* Well-organized test structure, layered by test suites, test categories, and test scripts.
* The framework is data-driven, not only with the inputs parameters but also at the verification against custom oracles.
* Extract data from specific portions of the response and use in subsequent requests.
* Perform several out-of-the-box validations on JSON responses, like response code, response headers etc.
* Inbuilt support for the JSON-path allows validating specific parts of the response, even at the most granular level.
* Validate the content, type, and even the structure of the response.  Thus, if the response isn't expected to contain a certain content in it, the tool can identify the precise location where it occurred.
* Tweak your template (no additional code to be written), and you're on your way to building some of the most accurate validations.
* Has a built-in parser for the templates, that can be customized to suit specific client needs.
* Generate pass-fail reports (with links to exported data), and comprehensive debug logs.
* Export JSON responses either in full or in part (using JSON-path) to readable CSV files, that can be used to further manually validate the response.
* Web support using Python-Flask.
