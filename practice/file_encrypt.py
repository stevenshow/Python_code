import os

from cryptography.fernet import Fernet

path = os.path.dirname(__file__)

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
    return open('key.key', 'rb').read()
