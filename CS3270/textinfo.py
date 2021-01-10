import string
import os
# [X] input any text file by user input ex. (yankee.txt)
# [X] Character count
# [X] Lower case count
# [X] Digit count
# [X] White space count
# [X] Vowels - {'a': 102, 'e': 165, 'i': 68, 'o': 93, 'u': 21} 
# [X] Consonants count
# [] Average words per sentence count (rounded to nearest 10th)

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
    vowels = {}
    consonants = 0
    digits = 0
    
    #Counts number of Vowels, Consonants, and Digits
    for letter in text:
        if letter.isalpha() and letter in vowel_chars:
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
    else:
        avg_wps = 0    
    
    print_text_info(character_count, upper_count, lower_count, 
        digits, white_space, vowels, consonants, sentences, avg_wps)

def print_text_info(characters, upper_case, lower_case, digits, white_space, vowels, consonants, sentences, avg_wps):
    print(f'''
    Characters:  {characters}
    Upper case:  {upper_case}
    Lower case:  {lower_case}
    Digits:      {digits}
    White space: {white_space}
    Vowels:      {vowels}
    Consonants:  {consonants}
    Sentences:   {sentences}
    Avg words per sentences: {avg_wps}''')

read_file()