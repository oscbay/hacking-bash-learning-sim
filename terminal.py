from asyncio import sleep

import cd
import clear
import createtxt
import rm
import os
import ls
import rm
import de_encryption
import shutil
from pathlib import Path


def get_command(user_data):
    hostname = user_data[1]
    username = user_data[0]
    path = os.getcwd()

    return input(f"{username}@{hostname}:~{path}$ ")


def command_operation(Sandbox, tokens, base_path):
    if not tokens:
        return

    current_path = os.getcwd()

    

    if tokens[0] == 'create':
        try:
            createtxt.create_txt(tokens)
        except PermissionError:
            print(f"Error: Permission denied to create file '{tokens[1]}'.")

    elif tokens[0] == 'write':
        try:
            createtxt.write_txt(tokens)
        except PermissionError:
            print(f"Error: Permission denied to write to file '{tokens[1]}'.")

    elif tokens[0] == 'txtencrypt':
            if len(tokens) < 2:
                print("Error: Please specify a txt to encrypt.")
            else:
                file_to_encrypt = ' '.join(tokens[1:])
                encrypted_data = de_encryption.encrypttxt(file_to_encrypt)
                try:
                    shutil.rmtree(tokens[1])
                except: 
                    try: os.path.isfile(tokens[1])
                    except: 
                        print("Error")

    elif tokens[0] == 'txtdecrypt':
        if len(tokens) < 2:
            print("Error: Please specify a txt to decrypt.")
        else:
            file_to_decrypt = ' '.join(tokens[1:])
            decrypted_data = de_encryption.decrypttxt(file_to_decrypt)
            try:
                shutil.rmtree(tokens[1])
            except: 
                try: os.path.isfile(tokens[1])
                except: 
                    print("Error")

    elif tokens[0] == 'encrypt':
        if len(tokens) < 2:
            print("Error: Please specify data to encrypt.")
        else:
            data_to_encrypt = ' '.join(tokens[1:])
            encrypted_data = de_encryption.encrypt(data_to_encrypt)
            print(f"Encrypted data: {encrypted_data}")
            os.mkdir(encrypted_data)
            try:
                shutil.rmtree(tokens[1])
            except: 
                try: os.path.isfile(tokens[1])
                except: 
                    print("Error")

    elif tokens[0] == 'decrypt':
        if len(tokens) < 2:
            print("Error: Please specify data to decrypt.")
        else:
            data_to_decrypt = ' '.join(tokens[1:])
            decrypted_data = de_encryption.decrypt(data_to_decrypt)
            print(f"Decrypted data: {decrypted_data}")
            os.mkdir(decrypted_data)
            shutil.rmtree(tokens[1])

    elif tokens[0] == 'cd':
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
            rm.rm(tokens, current_path)
        except IndexError:
            print("Error: Please specify a file or directory to remove.")
        except PermissionError:
            print(f"Error: Permission denied to access '{tokens[1]}'.")

    elif tokens[0] == 'clear':
        clear.clear_terminal()

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
        if len(tokens) < 2:
            print("Error: Please specify a directory name.")
        elif tokens[1] == '--help':
            print("Usage: mkdir [DIRECTORY]")
            print("Create a new directory named DIRECTORY.")
            print("  --help   display this help and exit")
        elif len(tokens) > 2:
            print("Error: Too many arguments.")
        else:
            try:
                os.mkdir(tokens[1])
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

    elif tokens[0] == '': #empty command, do nothing
        pass

    else: #error as no tokens as returned
        print(f"Error: Command '{tokens[0]}' not found.")