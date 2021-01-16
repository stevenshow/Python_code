'''Reads to file provided and counts all the letters and apostrophes,
then outputs to a file the count of each letter (case does not matter)'''
import re
# [] Read file
# [] Store file data and process file
# [] Count only words that have letters and apostrophes (everything lowercase)
# [] Output count and words in a nice column format

def count_words():
    with open("/home/steven/Documents/Python_code/CS3270/Exercise_2/Strings.txt") as f: 
        for line in f:
            for word in line.split():
                print(re.sub(r'\w*\d\w*', '', word).strip())

count_words()