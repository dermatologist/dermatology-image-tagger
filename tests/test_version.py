#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of DITagger.
# https://github.com/dermatologist/dermatology-image-tagger

# Licensed under the GPL license:
# http://www.opensource.org/licenses/GPL-license
# Copyright (c) 2016, Bell Eapen <github@gulfdoctor.net>

from preggy import expect

from DITagger import __version__
from tests.base import TestCase


class VersionTestCase(TestCase):
    def test_has_proper_version(self):
        expect(__version__).to_equal('0.1.0')
