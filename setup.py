#!/usr/bin/env python

from setuptools import setup

requires = ['bottle==0.12.7']

py_modules = ['hello']

packages = []

setup_options = dict(
    name='python-bottle-boilerplate',
    version='0.0.1',
    description='Boilerplate project for a deployable bottle service.',
    author='Anthony McClosky',
    author_email='anthony.mcclosky@gmail.com',
    install_requires=requires,
    py_modules=py_modules,
    packages=packages
)

setup(**setup_options)