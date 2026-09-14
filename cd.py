import os

def cd(command, sandbox, current_path, base_path):

    if command[1] == '-':

        if sandbox and current_path == base_path:
            print("Error: Cannot navigate above the base path in sandbox mode.")
        else:
            os.chdir('..')

    elif command[1] == '--help':
        print("Usage: cd [DIRECTORY]")
        print("Change the current directory to DIRECTORY.")
        print("  -   go to the previous directory")
        print("  --help   display this help and exit")

    elif command[1] == '/' and sandbox:
        print("Error: Cannot navigate to the root directory in sandbox mode.")


    else:
        os.chdir(command[1])

    return os.getcwd()