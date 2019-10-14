#-*- coding: utf-8 -*-

import os
from os.path import isfile

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

draw_tree("/home/coddy/bin/COPASI-4.15.95-Linux-64bit", "")