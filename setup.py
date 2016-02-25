# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='probe-py',
    version='1.0.0',
    packages=[
        'probe',
    ],
    author='Suraj Arya',
    author_email='suraj@loanzen.in',
    description='A python client for the probe apis.',
    url='https://github.com/loanzen/probe-py',
    license='MIT',

    install_requires=[
        "apiclient-requests"
    ],
)