#!/usr/bin/python
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


import os

'''
This script renames the current computation directory files to a prescribed one

It needs to be launched in the appropriate directory
'''

####### User Inputs #######

old_name = "DemoCase_1_SA_ExtWF_booster_uns" # To be modified

new_name = "DemoCase_1_SA_ExtWF_booster_uns_res" # To be modified

####### Main Program ######

#current_folder_path, current_folder_name = os.path.split(os.getcwd())

for filename in os.listdir(os.getcwd()):
    if filename.startswith(old_name):
        print("Renaming %s to %s ...") % (filename, new_name + filename[len(old_name):])
        os.rename(filename, new_name + filename[len(old_name):])

print ("Done")




