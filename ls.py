
import os

def ls(directory):
    "input = directory, output = list of files in directory"
    files = os.listdir(directory)
    if files:
        print('\n'.join(files))
    else:
        print("No files found.")