import os
import shutil
def rm (command, current_path):

    if command[1] == '-r':
        if os.path.isdir(command[2]):
            shutil.rmtree(command[2])
        elif os.path.isfile(command[2]):
            print(f'{command[2]} is a file.')
        else:
            print(f'Directory not found: {command[2]}')

    elif command[1] == '--help':
        print("Usage: rm [OPTION]... [FILE]...")
        print("Remove (unlink) the FILE(s).")
        print("  -r, --recursive   remove directories and their contents recursively")
        #print("  -f, --force       ignore nonexistent files and arguments, never prompt")
        print("  --help            display this help and exit")

    else:
        if os.path.isfile(command[1]):
            os.remove(command[1])
        elif os.path.isdir(command[1]):
            print(f'{command[1]} is a directory.')
        else:
            print(f'File not found: {command[1]}')