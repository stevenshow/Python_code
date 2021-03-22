#Password Generator
'''
[X]Grab user input on whether they want a 8 or 16 character password
[X]Generate password with Uppercase, lower case, special character, and number
[X]Copy generated password to clipboard for pasting
[]Ask if they would like to write the password to a file
[]Ask them to add that password to a specific program or website they are using
[]Encrypt that file so they can only read it with the program
'''
import random
import pyperclip

def get_input():
    length = input('Would you like your password to be 8 or 16 chars long?: ')
    while(length != '8' and length != '16'):
        length = input('Please enter either 8 or 16: ')
    return int(length)

def pass_generator():
    #if length is 8: (2 Upper)(2 Lower)(2 digits)(2 Special Characters)
    #if length is 16: (4 Upper)(4 Lower)(4 Digits)(4 Special Characters)
    length = get_input()
    multiplier = int(length/4)
    password = []
    for _ in range(multiplier):
        #random uppercase letter
        password.append(chr(random.randint(65,90)))
        #random lower case letter
        password.append(chr(random.randint(97,122)))
        #random number
        password.append(chr(random.randint(48,57)))
        #random special character
        password.append(chr(random.randint(33,50)))
    random.shuffle(password)
    #Makes list of characters into a string that can be inputted
    password_str = ''.join([str(elem) for elem in password])
    print(password_str)
    copy_to_clip = input('Would you like to copy this password to your clipboard? [Y/N]: ')
    if (copy_to_clip.lower() == 'y'):
        to_clipboard(password_str)
    else: 
        exit
    
    
def to_clipboard(password):
    #copies the password to the clipboard to be pasted in a password field
    pyperclip.copy(password)

pass_generator()