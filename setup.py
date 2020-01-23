# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='ilias2nbgrader',
    version='0.1',
    description='Exchange submissions and feedbacks between ILIAS and nbgrader',
    author='Tim Metzler',
    author_email='tim.metzler@h-brs.de',
    packages=find_packages(exclude=('tests', 'docs')),
    install_requires=[
        "fuzzywuzzy",
        "python-Levenshtein",
        "nbformat"
    ],
    include_package_data = True,
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose']
)