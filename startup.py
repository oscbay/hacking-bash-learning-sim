import os
import socket

def userid():
    "gets the username and hostname of the computer"

    username = os.getlogin()

    hostname = socket.gethostname()
    userinfo = [username, hostname]
    return userinfo