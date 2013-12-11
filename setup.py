"""nibbler-python - Better email parser

nibbler-python helps you parse for valid email addresses in Python projects

Example Usage
-------------
    from nibbler.parser import parse_email

    # valid email
    parse_email('"much.more unusual"@example.com')

    # invalid email
    parse_email('Abc.example.com')

Contribute
----------
This library is hosted on Github and you can contribute there:
https://github.com/sendgridlabs/nibbler-python
"""

from setuptools import setup, find_packages
from nibbler import __version__

doc = __doc__.splitlines()

dev_requirements = [
    # tests:
    'nose',
    'coverage',

    # docs:
    'Sphinx',
    'sphinx_rtd_theme',
    'sphinxcontrib-httpdomain',
    'livereload'
]

setup(
    name='nibbler-python',
    description=doc[0],
    long_description='\n'.join(doc[2:]),
    version=__version__,
    packages=find_packages(),
    extras_require={
        'dev': dev_requirements
    },
    author="Isaac Saldana",
    maintainer="Kien Pham",
    maintainer_email="kien@sendgrid.com",
    url="https://github.com/sendgridlabs/nibbler-python",
    keywords='email parser esp sendgrid',
    license="MIT",
    platforms="Posix; MacOS X; Windows",
    classifiers=["Development Status :: 5 - Production/Stable",
                 "Intended Audience :: Developers",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",
                 "Topic :: Internet",
                 "Programming Language :: Python :: 2",
                 "Programming Language :: Python :: 2.6",
                 "Programming Language :: Python :: 2.7"],
)
