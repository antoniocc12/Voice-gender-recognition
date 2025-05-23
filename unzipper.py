#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import tarfile

raw_folder = '/raw/'

for f in os.listdir(raw_folder):
    if f.endswith('.tgz'):
        tar = tarfile.open(os.path.join(raw_folder, f))
        tar.extractall(raw_folder)
        tar.close()
