import string
import os
# [X] input any text file by user input ex. (yankee.txt)
# [X] Character count
# [] Upper case letter count
# [] Lower case count
# [] Digit count
# [] White space count
# [] Vowels - {'a': 102, 'e': 165, 'i': 68, 'o': 93, 'u': 21} 
# [] Consonants count
# [] Average words per sentence count (rounded to nearest 10th)

def read_file():
    filename = input('Enter name of text file: ')
    with open('/home/steven/Documents/python_practice-1/CS3270/' + filename, 'r') as f:
        print(f'\nStatistics for file: {filename}:\n')
        text = f.read()
        textinfo(text)
    
    

def textinfo(text):
    #character_count = 0
    
    character_count = (for letter in text)
    
    for letter in text:
        character_count += 1
    upper_count = sum(map(str.isupper, text))
    lower_count = sum(map(str.islower, text))
    print(character_count, upper_count, lower_count)





read_file()