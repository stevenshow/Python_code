import string
import os
# [X] input any text file by user input ex. (yankee.txt)
# [X] Character count
# [X] Lower case count
# [X] Digit count
# [X] White space count
# [X] Vowels - {'a': 102, 'e': 165, 'i': 68, 'o': 93, 'u': 21} 
# [X] Consonants count
# [X] Average words per sentence count (rounded to nearest 10th)

def read_file():
    try:
        filename = input('Enter name of text file: ')
        with open('/home/steven/Documents/python_practice-1/CS3270/' + filename, 'r') as f:
            print(f'\nStatistics for file [{filename}]:')        
            text = f.read()
            text_info(text)
    except IOError:
        print('File does not exist, try a different file.')
        read_file()


def text_info(text):
    vowel_chars = 'aeiou'
    words = text.split()
    character_count = sum(1 for letter in text)    
    upper_count = sum(map(str.isupper, text))
    lower_count = sum(map(str.islower, text))
    white_space = sum(map(str.isspace, text))
    vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    consonants = 0
    digits = 0
    
    #Counts number of Vowels, Consonants, and Digits
    for letter in text:
        if letter.isalpha() and letter in vowel_chars:
            #this statement is if the vowel dictionary is not already populated with vowels
            if letter not in vowels:
                vowels[letter.lower()] = 1
            else: 
                vowels[letter.lower()] += 1 
        elif letter.isalpha() and letter not in vowel_chars:
            consonants += 1
        elif letter.isdigit():
            digits += 1
    
    counter_dict = {}
    counter = 0
    sen_count = -1
    #Could also get sentence count by doing len(counter_dict)
    for word in words:
        if word.endswith('.') == False:
            counter +=1
        else:
            counter +=1 
            sen_count += 1
            counter_dict[sen_count] = counter
            counter = 0
    
    if len(counter_dict) > 0:
        sentences = len(counter_dict)
        avg_wps = (sum(counter_dict.values())/ sentences)
        avg_wps = round(avg_wps, 1)
    else:
        sentences = 0
        avg_wps = 0    
    
    info = {'characters': character_count, 'upper': upper_count, 'lower': lower_count, 'digits': digits,
    'whitespace': white_space, 'vowels': vowels, 'consonants': consonants, 'sentences': sentences, 'avg_wps': avg_wps}
    print_text_info(info)

def print_text_info(info):
    print(f'''
    Characters:  {info['characters']}
    Upper case:  {info['upper']}
    Lower case:  {info['lower']}
    Digits:      {info['digits']}
    White space: {info['whitespace']}
    Vowels:      {info['vowels']}
    Consonants:  {info['consonants']}
    Sentences:   {info['sentences']}
    Avg words per sentences: {info['avg_wps']}''')

read_file()