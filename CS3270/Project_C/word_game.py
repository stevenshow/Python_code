from itertools import combinations
import random
import nltk
path = '/home/steven/Documents/Python_code/CS3270/Project_C/'
with open(path + 'words.txt', 'r') as f:
    file = f.read()
    words = nltk.word_tokenize(file)


word = 'burner'
letter_tuples = list(combinations(word, 3))
my_words = [''.join(tups) for tups in letter_tuples]
print(my_words)
