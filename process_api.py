#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
from apkil import api
import cPickle

levels = [17, 19, 20, 21]

for level in levels:

    jar_name = "android-%d.jar" % level
    jar_path = os.path.join("androidlib.new", jar_name)
    data_path = os.path.join("androidlib", "android-%d.db" % level)

    android_api = api.AndroidAPI(level, jar_path)
    android_api.save(data_path)


