from itertools import combinations
import random
import nltk
import string
import re
# [X] Parse text file and create list of words
# [X] Create dictionary with length and starting letter as key
# [X] Get user input to choose what word lengths to choose
# [X] Grab random word with specified length
# [X] Get remaining words with specified lengths from chosen words letters
# [] Create function to scramble word and get user guesses and quit on 'q'

low_high = re.sub('\D', '', input('Enter the range of word lengths (low,high): '))
low = int(low_high[0])
high = int(low_high[1:])

def get_user():
    pass

def choose_word(high, word_dict):
    '''Takes the high input and also gets a random letter to use as a tuple to search
    in the dictionary tuple keys'''
    letter = random.randint(97, 122)
    if word_dict[(chr(letter), high)]:
        word = word_dict[(chr(letter), high)][0]
    else:
        letter = random.randint(97, 122)
    return(word)

def dict_tuple():
    '''Creates a dictionary with (starting letter of word, length of word) as the key and
    the value as a list of words fitting that criteria.
    EX. {('a', 3): ['abs', 'art']'''
    path = '/home/steven/Documents/Python_code/CS3270/Project_C/'
    with open(path + 'words.txt', 'r') as f:
        word_dict = {}
        file = f.read()
        words = nltk.word_tokenize(file)
        for word in words:
            if (word[0].lower(), len(word)) in word_dict:
                word_dict[(word[0].lower(), len(word))].append(word.lower())
            else:
                word_dict[(word[0].lower(), len(word))] = [word.lower()]
        return(word_dict)

def process_dict(low, high, chosen_word, word_dict):
    word = chosen_word
    guess_list = set()
    for i in range(low, high):
        #words are not fully scrambling for every combination
        letter_tuples = list(combinations(word, i))
        my_words = [''.join(tups) for tups in letter_tuples]
        get_extra_words(my_words, guess_list)
    print(guess_list)


def get_extra_words(my_words, guess_list):
    for word in my_words:
        if (word[0], len(word)) in word_dict:
            if word in word_dict[(word[0], len(word))]:   
                guess_list.add(word)                



word_dict = dict_tuple()
choose_word(high, word_dict)
word = choose_word(high, word_dict)
process_dict(low, high, word, word_dict)
get_user()

def dict_creator():
    path = '/home/steven/Documents/Python_code/CS3270/Project_C/'
    with open(path + 'words.txt', 'r') as f:
        my_dict = {}
        file = f.read()
        words = nltk.word_tokenize(file)
        #print(words)
        for word in words:
            if word[0].lower() in my_dict:    
                my_dict[word[0].lower()].append(word.lower())
            else:
                my_dict[word[0].lower()] = [word.lower()]    
        print(my_dict)

    word = 'burner'
    letter_tuples = list(combinations(word, 3))
    my_words = [''.join(tups) for tups in letter_tuples]
    print(my_words)
    for word in my_words:
        if word[0] in my_dict:
            if word in my_dict[word[0]]:
                print(word)
    #print(my_words)
