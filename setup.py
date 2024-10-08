#!/usr/bin/env python
# encoding: utf-8

import sys
import os

try:
    from setuptools import setup, Extension
    setup, Extension
except ImportError:
    from distutils.core import setup, Extension
    setup, Extension

import numpy


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist upload")
    sys.exit()


desc = open("README.rst").read()
required = ["numpy"]

include_dirs = [
    "acor",
    numpy.get_include(),
]
extra_compile_args = [
    '-Wno-incompatible-pointer-types',
]
acor = Extension("acor._acor", ["acor/_acor.c", "acor/acor.c"],
                 extra_compile_args=extra_compile_args,
                 include_dirs=include_dirs)


setup(
    name="acor",
    version="1.1.1",
    author="Daniel Foreman-Mackey and Jonathan Goodman",
    author_email="danfm@nyu.edu",
    packages=["acor"],
    url="http://github.com/dfm/acor",
    license="MIT",
    description="Estimate the autocorrelation time of a time series quickly.",
    long_description=desc,
    install_requires=required,
    ext_modules=[acor],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
