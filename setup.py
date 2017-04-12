#!/usr/bin/env python

from setuptools import setup

setup(
    # GETTING-STARTED: set your app name:
    name='BhoomiPutra',
    # GETTING-STARTED: set your app version:
    version='1.0',
    # GETTING-STARTED: set your app description:
    description='OpenShift App',
    # GETTING-STARTED: set author name (your name):
    author='Vishnu Dutt',
    # GETTING-STARTED: set author email (your email):
    author_email='vishnubishnoi7@gmail.com',
    # GETTING-STARTED: set author url (your url):
    url='http://www.bhoomiputra.in/',
    # GETTING-STARTED: define required django version:
    install_requires=[
        'Django==1.8.4'
    ],
    dependency_links=[
        'https://pypi.python.org/simple/django/'
    ],
)
