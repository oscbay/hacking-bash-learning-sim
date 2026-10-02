import tokenizer

import startup
import terminal
import os

Sandbox = True #enable this to run the program in a sandboxed environment, which will prevent it from making changes to your real file system.
Gui = True #enable this to run the program with a GUI, which will allow you to enter commands in a graphical interface.


def get_sandbox():
    return Sandbox

def get_gui_toggle():
    return Gui

if not os.path.exists('sim_environment') and Sandbox:
    os.mkdir('sim_environment')

if Sandbox:
    os.chdir('sim_environment')

base_path = os.getcwd()


print('''Welcome to the hacking simulator!
Please note that this is going to use your real computer\'s file system, so be careful!
Because of this fact please delete files at your own risk.

To get started please use the command 'help'
''')
while True:
    command = terminal.get_command(startup.userid())

    tokens = tokenizer.tokenize(command)

    terminal.command_operation(Sandbox, tokens, base_path)
