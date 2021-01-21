import re
'''Reads to file provided and counts all the letters and apostrophes,
then outputs to a file the count of each letter (case does not matter)'''
# [] Read file
# [] Store file data and process file
# [] Count only words that have letters and apostrophes (everything lowercase)
# [] Output count and words in a nice column format
def count_words():
    word_pattern = '[A-Za-z\']+'
    print(word_pattern)
    with open("/home/steven/Documents/Python_code/CS3270/Exercise_2/Strings.txt") as f: 
        file = f.read()
        my_list = re.findall(word_pattern, file)
        print(my_list)
        

count_words()
