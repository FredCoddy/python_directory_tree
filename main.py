#-*- coding: utf-8 -*-

import argparse
import os
from os.path import isfile

parser = argparse.ArgumentParser(description='Draw hierarchical tree')
parser.add_argument("path", help="Absolute path to the root directory")


path = os.getcwd() # get the working directory
spacing = ""

def draw_tree(path, spacing):
    '''
    List recursively files and directories from the working directory.
    '''
    dir_content = os.listdir(path) # list all files + directories in `path`
    spacing += "\t"
    for elem in dir_content :
        if isfile(f"{path}/{elem}") is True: # `isfile()` Test whether a path is a regular file (return True if regular file)
            print(f"{spacing} |_ {elem}")
        else:
            print(f"{spacing} |_ {elem}")
            draw_tree(f"{path}/{elem}", spacing)

args = parser.parse_args()
draw_tree(args.path, "")
