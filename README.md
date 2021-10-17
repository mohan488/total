# Total
 
Project micro-service is used to get the sum of a list of numbers, the service processes all the requests asynchronously. written in Python/FastAPI


## Content

1. [Core Dependencies](#cd)
2. [Getting Started](#gs)
3. [Running the Server](#rts) 
4. [Testing](#t)
5. [Unit Tests](#ut)

<a name="cd"></a>
### 1. Core Dependencies

    * Python Version 3.8
    * FastAPI Version 0.7


<a name="gs"></a>
### 2. Getting Started

Note: explicit commands may differ depending on your OS.

    * Install Python from https://www.python.org/downloads/
    
    * clone the Pull project from https://github.com/mohan488/total
    
    * Setup a virtualenv in your preferred fashion e.g.:
    	$ python3 -m venv total
    	$ source total/bin/activate

    * You can install all the dependencies with:
        $ pip install -r requirements.txt


<a name="rts"></a>
### 3. Running the Server:

    Navigate to the `totals` folder and run the following command. python3 main.py navigate to http://127.0.0.1:4658/ to go to the home page.


<a name="rts"></a>
### 4. Testing:

    For initial testing with API, swagger integrated with the FastAPI server. navigate to http://127.0.0.1:4658/ to go to the swagger and docs page.


<a name="ut"></a>
### 5. Unit Tests:

    The tests run with **Pytest**.
    Navigate to the `totals` folder and run the following command `pytest -vv`.
    you can enable test coverage HTML report generation by passing --cov-report=html.
