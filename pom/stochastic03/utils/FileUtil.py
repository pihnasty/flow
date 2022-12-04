import os
import os.path as path

def make_dir_if_not(fileName):
    if not path.isdir(fileName):
        os.makedirs(fileName)
