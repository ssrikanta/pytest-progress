pytest-progress
================


pytest-progress is a plugin for `py.test <http://pytest.org>`_ that allows to 
print the test progress like number of tests Passed , Failed, Skipped and also 
instant test failure messages.


Requirements
------------

You will need the following prerequisites in order to use pytest-progress:

- Python 2.7, 3.4 or 3.5
- pytest 2.9.0 or newer



Installation
------------

To install pytest-progress::

    $ pip install pytest-progress

Then run your tests with::

    $ py.test --show-progress

If you would like more detailed output (one test per line), then you may use the verbose option::

    $ py.test --verbose


Examples
------------
To run the pytest with progress::

	$ py.test --show-progress test_progress_report.py
	$ py.test --showprogress test_progress_report.py
	
To run tests in verbose mode::

	$ py.test --show-progress --verbose test_progress_report.py
	$ py.test --showprogress --verbose test_progress_report.py
