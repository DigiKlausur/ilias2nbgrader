# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

setup(
    name='ilias2nbgrader',
    version='0.3',
    license='MIT',
    description='Exchange submissions and feedbacks between ILIAS and nbgrader',
    long_description=readme,
    long_description_content_type="text/markdown",
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
    test_suite='tests',
    tests_require=['pytest-cov']
)