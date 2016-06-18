#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of DITagger.
# https://github.com/dermatologist/dermatology-image-tagger

# Licensed under the GPL license:
# http://www.opensource.org/licenses/GPL-license
# Copyright (c) 2016, Bell Eapen <github@gulfdoctor.net>

from setuptools import setup, find_packages
from DITagger import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(
    name='DITagger',
    version=__version__,
    description='Dermatology Image Tagger',
    long_description='''
Dermatology Image Tagger
''',
    keywords='dermatology, image organizer, clinical',
    author='Bell Eapen',
    author_email='github@gulfdoctor.net',
    url='https://github.com/dermatologist/dermatology-image-tagger',
    license='GPL',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GPL License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pyqt',
        'matplotlib',
        'opencv',
        'pyopengl',
        'visvis',
        'pyforms',
        'esky',
        'pil',
        'piexif',

        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],
    extras_require={
        'tests': tests_require,
    },
    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'DITagger=DITagger.cli:main',
        ],
    },
)
