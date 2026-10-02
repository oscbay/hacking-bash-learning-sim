from asyncio import sleep

import cd
import clear
import rm
import os
import ls
import rm

def get_command(user_data):
    hostname = user_data[1]
    username = user_data[0]
    path = os.getcwd()

    return input(f"{username}@{hostname}:~{path}$ ")


def command_operation(Sandbox, tokens, base_path):
    
    current_path = os.getcwd()

    if tokens[0] == 'cd':
        try:
            current_path = cd.cd(tokens, sandbox=Sandbox, base_path=base_path, current_path=current_path)
        except IndexError:
            print("Error: Please specify a directory.")
        except PermissionError:
            print(f"Error: Permission denied to access '{tokens[1]}'.")
        except FileNotFoundError:
            print(f"Error: Directory '{tokens[1]}' not found.")

    elif tokens[0] == 'rm':
        try:
            rm.rm(tokens, current_path )
        except IndexError:
            print("Error: Please specify a file or directory to remove.")
        except PermissionError:
            print(f"Error: Permission denied to access '{tokens[1]}'.")

    elif tokens[0] == 'clear': clear.clear_terminal()

    elif tokens[0] == 'ls':
        try:
            ls.ls(current_path)
        except IndexError:
            print("Error: Please specify a directory to enter.")

    elif tokens[0] == 'exit':
        print("Exiting the terminal...")
        sleep(5)
        exit()

    elif tokens[0] == 'mkdir':
        try:
            os.mkdir(tokens[1])
        except IndexError:
            print("Error: Please specify a directory name.")
        except FileExistsError:
            print(f"Error: Directory '{tokens[1]}' already exists.")
        except PermissionError:
            print(f"Error: Permission denied to create directory '{tokens[1]}'.")

    elif tokens[0] == 'help':
        print("Available commands:")
        print("cd - Change the current directory.")
        print("rm - Remove a file or directory.")
        print("clear - Clear the terminal screen.")
        print("ls - List files and directories in the current directory.")
        print("exit - Exit the terminal.")
        print("mkdir - Create a new directory.")
        print("help - Show this help message.")
        print("command --help - Show help for a specific command.")

    elif tokens[0] == '':
        pass

    else:
        print(f"Error: Command '{tokens[0]}' not found.")