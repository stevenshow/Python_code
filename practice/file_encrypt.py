import os
import sys
from cryptography.fernet import Fernet

#path = os.path.dirname(__file__)
path = os.path.dirname(os.path.abspath(__file__)) + '/'

def get__user_file(user_file):
    '''Checks file path and returns path if exists, exits if not'''
    if '/' in user_file:
        if os.path.isfile(user_file):
            print('File exists')
            return user_file
        else:
            print('File in ' + user_file + ' does not exist!')
            sys.exit()
    else:
        if os.path.isfile(path + user_file):
            print('File exists')
            return path + user_file
        else:
            print('File in ' + path + user_file + ' does not exist!')
            sys.exit()

def create_key():
    '''Generates key and saves it to a file'''
    # [] Get where the user would like to save the key (Directory full path, specified paths, USB possibly?)
    #input('Would you like to save the key to [1]Documents or [2]Downloads? ')
    key = Fernet.generate_key()
    with open(path + 'key.key', 'wb') as key_file:
        key_file.write(key)


def read_key():
    '''Loads key in the current directory'''
    # [] Let user input where key is located as well as name of key file
    # [] Search user provided directory for files that contain key and try each?
    return open(path + 'key.key', 'rb').read()


def string_encrypt(str_encrypt):
    '''Encrypts a string that is passed'''

    # Creates key if one does not exist in the current directory
    if not os.path.isfile(path + 'key.key'):
        print('Created key in ' + path + ' as ' + 'key.key')
        create_key()
    key = read_key()
    f = Fernet(key)

    # Encodes the message into bytes suitable for encryption
    message = str_encrypt.encode()
    # Encrypts the message
    encrypted = f.encrypt(message)
    return encrypted


def string_decrypt(str_decrypt):
    '''Decrypts an encoded string that is passed'''
    if not os.path.isfile(path + 'key.key'):
        print('No key in working directory to decrypt wtih!')
    key = read_key()
    f = Fernet(key)
    return f.decrypt(str_decrypt).decode()


def file_encrypt(filename, key):
    '''Given a filename (str) and key (bytes), it encrypts the file and write it'''
    f = Fernet(key)
    # Encrypt data from file
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    # Overwrites data file with encrypted data
    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def file_decrypt(filename, key):
    '''Given a filename (str) and key (bytes), it decrypts the file and writes it'''
    f = Fernet(key)
    # Decrypts data from file
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    # Overwrites data file with decrypted data
    with open(filename, 'wb') as file:
        file.write(decrypted_data)


def main():
    # Creates key if one does not exist in the current directory
    if not os.path.isfile(path + '/key.key'):
        print('Created key in working directory as key.key')
        create_key()
        key = read_key()
    else:
        print('Key file already present')
        key = read_key()
    user_file_path = input('Enter the file name (If not in working directory, provided /full/path/to/file): ')
    user_file = get__user_file(user_file_path)
    user = input('Do you want to (1)Encrypt or (2)Decrypt the file? ')
    if user == '1':
        file_encrypt(user_file, key)
    if user == '2':
        file_decrypt(user_file, key)

if __name__ == '__main__':
    main()
