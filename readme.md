# warbler

Warbler is a Python Message Feed Application built with Flask, Jinja, and PostgreSQL.

## Prerequisites

You will need to have the following items installed in order to run this program:

1. Install Python (Version >= 3.6) and PiP Install Requirements
2. Install PostgreSQL
3. Create databases for application

- warbler
- warbler-test (if you want to run the tests)

## Getting Started

1. Clone the repo and Create Virtual Env for Application and load into it (while in the cloned repo directory)

	```
	$ python3 -m venv venv
	$ source ./venv/bin/activate
	```

2. 	Install the packages in requirements.txt.

   ```
   $ pip install -r requirements.txt
   ```

3. Start server instance by using flask run

   ```
   $ flask run
   ```

4. Create databases mentioned above in PostgreSQL

   For production database

   ```
   $ createdb warbler
   ```

   (Optional) - Only if you plan to run tests and need data

   ```
   $ createdb warbler-test
   ```

5. (Optional) - Load sample data into tables

   For production database:

   ```
   $ psql warbler < data.sql
   ```

   For test database:

   ```
   $ psql warbler-test < data.sql
   ```

## Running Tests

* All tests:
  `python -m unittest`

* Specific test:
  `python -m unittest  <insert testfile name here>`  


## Built With

- Python 3.6 - Server Language
- Flask - Flask Web Framework
- Jinja2 - HTML Templating Library
- bcrypt - Password Encryption Library
- SQLAlchemy - ORM for PostgreSQL
- psycopog2 - PostgreSQL adapter for Python
- WTForms & Flask-WTF - Form validation Library

Testing stack:

- python3 -m unittest

## Authors

- WongCo - https://github.com/wongco
- chad-schroeder - https://github.com/chad-schroeder
