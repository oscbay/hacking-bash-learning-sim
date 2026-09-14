
import os

def ls(directory):
    "input = directory, output = list of files in directory"
    print('\n'.join(os.listdir(directory)))