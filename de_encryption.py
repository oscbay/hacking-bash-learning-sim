def encrypttxt(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    data = encrypt(data)
    with open(file_path, 'w') as f:
        f.write(data)
    return data

def decrypttxt(file_path):
    with open(file_path, 'r') as f:
        data = f.read()
    data = decrypt(data)
    with open(file_path, 'w') as f:
        f.write(data)
    return data

def encrypt (data):

    encrypted_data = ""
    for char in data:
        if char == 'a':
            encrypted_data += 'c'
        if char == 'b':
            encrypted_data += 'd'
        if char == 'c': 
            encrypted_data += 'e'
        if char == 'd':
            encrypted_data += 'f'
        if char == 'e':
            encrypted_data += 'g'
        if char == 'f': 
            encrypted_data += 'h'
        if char == 'g':
            encrypted_data += 'i'
        if char == 'h':
            encrypted_data += 'j'
        if char == 'i':
            encrypted_data += 'k'
        if char == 'j':
            encrypted_data += 'l'
        if char == 'k':
            encrypted_data += 'm'
        if char == 'l':
            encrypted_data += 'n'
        if char == 'm':
            encrypted_data += 'o'
        if char == 'n':
            encrypted_data += 'p'
        if char == 'o':
            encrypted_data += 'q'
        if char == 'p':
            encrypted_data += 'r'
        if char == 'q':
            encrypted_data += 's'
        if char == 'r':
            encrypted_data += 't'
        if char == 's':
            encrypted_data += 'u'
        if char == 't':
            encrypted_data += 'v'
        if char == 'u':
            encrypted_data += 'w'
        if char == 'v':
            encrypted_data += 'x'
        if char == 'w':
            encrypted_data += 'y'
        if char == 'x':
            encrypted_data += 'z'
        if char == 'y':
            encrypted_data += 'a'
        if char == 'z':
            encrypted_data += 'b'
        if char == ' ':
            encrypted_data += ' '
        if char == '.':
            encrypted_data += '.'
        if char == ',':
            encrypted_data += ','
        if char == '!':
            encrypted_data += '!'
        if char == '?':
            encrypted_data += '?'
        if char == '@':
            encrypted_data += '@'
        if char == '#':
            encrypted_data += '#'
        if char == '$':
            encrypted_data += '$'
        if char == '%':
            encrypted_data += '%'
        if char == '^':
            encrypted_data += '^'
        if char == '&':
            encrypted_data += '&'
        if char == '*':
            encrypted_data += '*'
    return encrypted_data

def decrypt (data):
    
    decrypted_data = ""
    for char in data:
        if char == 'a':
            decrypted_data += 'y'
        if char == 'b':
            decrypted_data += 'z'
        if char == 'c': 
            decrypted_data += 'a'
        if char == 'd':
            decrypted_data += 'b'
        if char == 'e':
            decrypted_data += 'c'
        if char == 'f': 
            decrypted_data += 'd'
        if char == 'g':
            decrypted_data += 'e'
        if char == 'h':
            decrypted_data += 'f'
        if char == 'i':
            decrypted_data += 'g'
        if char == 'j':
            decrypted_data += 'h'
        if char == 'k':
            decrypted_data += 'i'
        if char == 'l':
            decrypted_data += 'j'
        if char == 'm':
            decrypted_data += 'k'
        if char == 'n':
            decrypted_data += 'l'
        if char == 'o':
            decrypted_data += 'm'
        if char == 'p':
            decrypted_data += 'n'
        if char == 'q':
            decrypted_data += 'o'
        if char == 'r':
            decrypted_data += 'p'
        if char == 's':
            decrypted_data += 'q'
        if char == 't':
            decrypted_data += 'r'
        if char == 'u':
            decrypted_data += 's'
        if char == 'v':
            decrypted_data += 't'
        if char == 'w':
            decrypted_data += 'u'
        if char == 'x':
            decrypted_data += 'v'
        if char == 'y':
            decrypted_data += 'w'
        if char == 'z':
            decrypted_data += 'x'
        if char == ' ':
            decrypted_data += ' '
        if char == '.':
            decrypted_data += '.'
        if char == ',':
            decrypted_data += ','
        if char == '!':
            decrypted_data += '!'
        if char == '?':
            decrypted_data += '?'
        if char == '@':
            decrypted_data += '@'
        if char == '#':
            decrypted_data += '#'
        if char == '$':
            decrypted_data += '$'
        if char == '%':
            decrypted_data += '%'
        if char == '^':
            decrypted_data += '^'
        if char == '&':
            decrypted_data += '&'
        if char == '*':
            decrypted_data += '*'
    return decrypted_data