import os
from os.path import isfile

class DirectoryTree:
    def __init__(self, path, space):
        self.path = path
        self.space = space


    def draw_tree(self, path, spacing):
        '''
        List recursively files and directories from the working directory.
        '''
        dir_content = os.listdir(path)  # list all files + directories in `path`
        spacing += "\t"
        for elem in dir_content:
            # `isfile()` Test whether a path is a regular file (return True if regular file)
            if isfile(f"{path}/{elem}") is True:
                print(f"{spacing} |_ {elem}")
            else:
                print(f"{spacing} |_ {elem}")
                self.draw_tree(f"{path}/{elem}", spacing)
