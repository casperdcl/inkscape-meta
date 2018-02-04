#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="inkscape",
    version="0.91 r13725",
    description="meta-package to remind me of inkscape dependencies",
    url="localhost://ubuntu16.04/py27/aptitude",
    author="Casper da Costa-Luis",
    author_email="casper.dcl@physics.org",
    install_requires="bs4 chardet html5lib lxml numpy six".split(),
)
