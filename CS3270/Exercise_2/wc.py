'''Reads to file provided and counts all the letters and apostrophes,
then outputs to a file the count of each letter (case does not matter)'''
import re
# [] Read file
# [] Store file data and process file
# [] Count only words that have letters and apostrophes (everything lowercase)
# [] Output count and words in a nice column format
def count_words():
    with open("/home/steven/Documents/Python_code/CS3270/Exercise_2/Strings.txt") as f: 
        file = f.read()
        word_count = {}
        word_list = (re.findall('([A-Za-z\']+)', file))
        for word in word_list:
            if word not in word_count:
                word_count[word] += 1
            else:
                word_count[word] += 1

    print(word_count)

count_words()