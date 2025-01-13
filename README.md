# Playwright - Python

- Versions used in training
    - Playwright 1.46
    - Python 3.12

https://github.com/microsoft/playwright-python

<pre>
PACKAGES:
pip install playwright #To perform clicks, etc.
pip install pytest #To run any kind of test

pip install pytest-playwrite  # Installs both packages, PLUS extra functionality!
</pre>

Very important to use a Virtual Environment!

<pre>srussel0@development:~/repos/python-playwright$ source .venv/local/bin/activate
sudo apt-get install libgstreamer1.0-0 gstreamer1.0-plugins-base gstreamer1.0-plugins-good gstreamer1.0-plugins-bad gstreamer1.0-plugins-ugly gstreamer1.0-libav
pip install -r requirements.txt
playwright install  # Installs browsers
</pre>

Run playwright scripts using pytest:

<pre>pytest .\demo.py</pre>

pytest.ini file for configuration:
<pre>
[pytest]
markers = 
    smoke: part of the smoke test suite
addopts = --headed --browser chromium --browser firefox --screenshot only-on-failure --numprocesses auto

# To execute pytest using markers:
pytest -m smoke # Pytest will run only those markers with the specified marker
</pre>

Error running playwright install:
<pre>
║ Host system is missing dependencies to run browsers. ║
║ Missing libraries:                                   ║
║     libgstcodecparsers-1.0.so.0                      ║
║     libavif.so.13 
</pre>

Running an html server using python:
<pre>
# Important to run from web directory!
srussel0@development:~/repos/python-playwright/web$ python -m http.server &  # runs on port 8000, if you need a different port:
srussel0@development:~/repos/python-playwright/web$ python -m http.server 3000 &
Then navigate browser to http://localhost:8000
</pre>

pytest discovery conventions:
- pytest searches directories containing test_*.py or *_test.py files

Find by iframe:

use .frame_locator('#foo')

## Using Playwright codegen
<pre>
$ playwright codegen http://localhost:8000
</pre>

This opens the webpage and Playwright inspector and lets you dynamically change the code by changing elements in the page

### Dialogs and Alerts
- Playwright dismisses dialogs by default

### Screenshots and seeing print statements
<pre>
$ pytest --screenshot only-on-failure test.py -rP #always run with -rP to see print statement
</pre>

### Session Scope - conftest.py ####
- move all session scope to a file conftest.py  # Must be named this, applies to current directory and all subdirectories.  Put in tests folder to apply to all tests
- It is normal to have multiple conftest.py files in a project
<pre>
import pytest

@pytest.fixture(scope='session', autouse=True) # Now runs once before all tests
def global_setup_available_everywhere():
    print('Global setup for entire test run of ALL applicable tests')
</pre>





