nibbler-python
==============
Better email parser for Python

[![Build Status](https://travis-ci.org/sendgridlabs/nibbler-python.png?branch=master)](https://travis-ci.org/sendgridlabs/nibbler-python)

![nibbler](doc/_static/nibbler.gif)

Installation
------------
	# Production: install from PyPI
	$ pip install nibbler-python
	
	# Development: if you want to contribute to this project, clone it, install it from source
	$ make install

Usage
-----
Please see the [test/test_parser.py](test/test_parser.py) for more test cases

	from nibbler.parser import parse_email

	# valid email
	parse_email('"much.more unusual"@example.com')

	# invalid email
	parse_email('Abc.example.com')


Testing
-------
	$ make test
