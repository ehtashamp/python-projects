"""
This program accepts a directory from the user and removes empty files from it.
It uses OS pacakge and its functions
"""
import os
dir_name = (input('Provide a a directory name to remove empty file form: '))
if os.path.isdir((dir_name)):
    all_files = os.listdir(dir_name)
    for file in all_files:
        filename = os.path.join(dir_name, file)
        if os.path.isfile(filename):
            if os.path.getsize(filename) == 0:
                os.remove( filename)
                print('removed file %d', filename)
