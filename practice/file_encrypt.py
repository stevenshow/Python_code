import os

from cryptography.fernet import Fernet

#path = os.path.dirname(__file__)
path = os.path.dirname(os.path.abspath(__file__)) + '/'


def create_key():
    '''Generates key and saves it to a file'''
    # [] Get where the user would like to save the key (Directory full path, specified paths, USB possibly?)
    #input('Would you like to save the key to [1]Documents or [2]Downloads? ')

    key = Fernet.generate_key()
    with open(path + '/key.key', 'wb') as key_file:
        key_file.write(key)


def read_key():
    '''Loads key in the current directory'''
    # [] Let user input where key is located as well as name of key file
    # [] Search user provided directory for files that contain key and try each?
    return open(path + '/key.key', 'rb').read()


def string_encrypt(str_encrypt):
    '''Encrypts a string that is passed'''

    # Creates key if one does not exist in the current directory
    if not os.path.isfile(path + '/key.key'):
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
    if not os.path.isfile(path + '/key.key'):
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
    else:
        print('Key file already present')
    user = input('What would you like to do? ')
    print(user)

if __name__ == '__main__':
    main()
