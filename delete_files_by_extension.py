#!/usr/bin/env python

# Copyright (c) 2018 Thanos Poulos
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

__version__ = '0.1'  
__author__ = 'Thanos Poulos'
__license__ = 'MIT'

######################################################################
#
# Script for deleting files with a specific extensions 
#
# 2017/06/14 - Thanos Poulos
#
######################################################################


import os

# This script needs to be run in the Design3D computation directory

# USER INPUT: extensions of files to delete
extensions = [".cgns"]

current_dir = os.getcwd()

# Do this process for each quantity
for ext in extensions:
        print("[Info] Deleting %s files") % (ext)
        # Go through all lower directories
        for folder, subfolder, files in os.walk(current_dir):
            for filename in files:
                # Open the quantity file and extract the quantity
                if filename.endswith(ext):
                    full_path = os.path.join(folder, filename)
                    print("Deleting %s") % full_path
                    os.unlink(full_path)
        print("[Info] Finished deleting %s files") % (ext)
