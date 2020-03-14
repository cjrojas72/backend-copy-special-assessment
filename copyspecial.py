#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys

# This is to help coaches and graders identify student assignments
__author__ = "Christian Rojas"


# +++your code here+++
# Write functions and modify main() to call them
def special_paths(dir):

    special_files = []

    for item in dir:
        if re.search(r'__(\w+)__', item):
            special_files.append(item)
    
    return special_files

   




def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser(description='Search for special files')
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('--dir', help='directory to search for files')
    # TODO need an argument to pick up 'from_dir'
    args = parser.parse_args()

    search_dir = args.dir
    todir = args.todir
    tozip = args.tozip

    file_list = os.listdir(search_dir)

    special_list = special_paths(file_list)

    tempDir = 'tempDir'

    full_path = os.path.join(todir, tozip)

    print full_path

    if todir:
        if tozip:
               paths = list(special_list)
               command = "zip -j {} {}".format(tozip, ' '.join(paths))
               print(command)
               os.system(command)

    else:
         if not os.path.exists(tempDir):
            print('need a directory to place special files')  
            os.mkdir('tempDir')
            print('Directory tempDir created') 

            for f in special_list:
                with open(os.path.join(tempDir, 'temp.zip'),'wb') as z:
                    z.write(f)
            
        

    # TODO you must write your own code to get the cmdline args.
    # Read the docs and examples for the argparse module about how to do this.
    
    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
