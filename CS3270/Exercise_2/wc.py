'''Reads to file provided and counts all the letters and apostrophes,
then outputs to a file the count of each letter (case does not matter)'''
import re
# [X] Read file
# [X] Store file data and process file
# [X] Count only words that have letters and apostrophes (everything lowercase)
# [X] Output count and words in a nice column format
def count_words():
    with open("/home/steven/Documents/Python_code/CS3270/Exercise_2/Strings.txt") as f: 
        file = f.read()
        word_count = {}
        word_list = (re.findall('([A-Za-z\']+)', file.lower()))
        longest_word = max(map(len, word_list))
        for word in word_list:
            if word not in word_count:
                word_count[word] = 1
            else:
                word_count[word] += 1
        sorted_word_count = sorted(word_count.items(), key =lambda x:x[1], reverse = True)
        for item in sorted_word_count:
            print('{0:>{1}}: {2:^5}'.format(item[0], longest_word ,item[1]))
count_words()