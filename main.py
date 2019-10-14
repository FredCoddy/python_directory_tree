#-*- coding: utf-8 -*-

import argparse

from tree import DirectoryTree

parser = argparse.ArgumentParser(description='Draw hierarchical tree')
parser.add_argument("path", help="Absolute path to the root directory")


args = parser.parse_args()
my_directory_tree = DirectoryTree(args.path, "")
my_directory_tree.draw_tree(args.path, "")
