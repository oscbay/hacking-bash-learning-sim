import startup
import terminal
import os
import random

Sandbox = True #enable this to run the program in a sandboxed environment, which will prevent it from making changes to your real file system.

print('''Welcome to the hacking simulator!
Please note that this is going to use your real computer\'s file system, so be careful!
Because of this fact please delete files at your own risk.''')


terminal.terminal(startup.userid(), Sandbox)
