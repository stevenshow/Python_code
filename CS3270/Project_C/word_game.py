'''Chooses a word based on user input and grabs all the substrings of that word
based on user input.  The user is then prompted to enter guesses and if the user
is correct the dashed word will be replaced with the users correct guess
if the user is wrong, the program will shuffle the word and let the user
guess again.  If the user is done guessing and wants to exit, they can enter
'q' and all the words will be revealed and the program will exit
Created by: Steven Schoebinger 2/01/2021'''
from itertools import combinations
import random
import re
import copy
import sys
import nltk
# pylint: disable=invalid-name, undefined-loop-variable
# [X] Parse text file and create list of words
# [X] Create dictionary with length and starting letter as key
# [X] Get user input to choose what word lengths to choose
# [X] Grab random word with specified length
# [X] Get remaining words with specified lengths from chosen words letters
# [X] Create function to scramble word and get user guesses and quit on 'q'

low_high = re.sub(r'\D', '', input('Enter the range of word lengths (low,high): '))
low = int(low_high[0])
high = int(low_high[1:])

def get_user():
    '''Gets the user input and gives feedback on correct word or not
    if the user is correct it will replcae the dashes with the correct word
    if the user is incorrect it will say try again and shuffle the word'''
    total = (sum([len(dotted_words[x]) for x in dotted_words if isinstance(dotted_words[x], list)]))
    correct = 0
    while True:
        last_shuffle = shuffle()
        if shuffle() != last_shuffle:
            print('\n' +
            shuffle() + ':\n')
        else:
            break
        for i in dotted_words:
            print(dotted_words[i])
        guess = input('\nEnter a guess: ')
        if guess == 'q':
            print('\n')
            for i in sorted_words:
                print(sorted_words[i])
            sys.exit()
        if len(guess) in sorted_words:
            if guess in sorted_words[len(guess)]:
                print('Correct!')
                correct += 1
                index = sorted_words[len(guess)].index(guess)
                dotted_words[len(guess)][index] = guess
            else:
                print('Try again!')
        else:
            print('Try again')
        if correct == total:
            print('\n')
            for i in dotted_words:
                print(dotted_words[i])
            sys.exit()

def shuffle():
    '''Shuffles the word each time that the user guesses a word'''
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return shuffled_word

def choose_word():
    '''Takes the high input and also gets a random letter to use as a tuple to search
    in the dictionary tuple keys'''
    chosen_word = ''
    word_list = []
    dict_keys = list(word_dict.keys())
    for x in dict_keys:
        if x[1] == high:
            word_list.append(x)
    choice = random.choice(word_list)
    chosen_word = random.choice(word_dict[choice])
    return chosen_word

def dict_tuple():
    '''Creates a dictionary with (starting letter of word, length of word) as the key and
    the value as a list of words fitting that criteria.
    EX. {('a', 3): ['abs', 'art']'''
    path = '/home/steven/Documents/Python_code/CS3270/Project_C/'
    with open(path + 'words.txt', 'r') as f:
        word_tup = {}
        file = f.read()
        words = nltk.word_tokenize(file)
        for ele in words:
            if (ele[0].lower(), len(ele)) in word_tup:
                word_tup[(ele[0].lower(), len(ele))].append(ele.lower())
            else:
                word_tup[(ele[0].lower(), len(ele))] = [ele.lower()]
        return word_tup

def process_dict(guess_list):
    '''Scrambles chosen word and creates subset of all words of length
    low->high+1'''
    lengths = set()
    guess_list = set()
    for i in range(low, high+1):
        letter_tuples = list(combinations(word, i))
        words = [''.join(tups) for tups in letter_tuples]
        process_dict_helper(words, guess_list, lengths)
    return lengths, guess_list

def process_dict_helper(words, guess_list, lengths):
    '''Helper function for process_dict() to place words into list'''
    for ele in words:
        if (ele[0], len(ele)) in word_dict:
            if ele in word_dict[(ele[0], len(ele))]:
                guess_list.add(ele)
                lengths.add(len(ele))

def dotted_list(words, lengths):
    '''Creates two dictionaries.  One is the dictinoary with key(len of word):
    value(words in alphabetical order.  The other dictionary is a deep copy
    of the first dictionary with all the words replaced with '-' for guessing.'''
    sort_words = sorted(list(words))
    sorted_dict = {i: [] for i in lengths}
    for ele in sort_words:
        sorted_dict[len(ele)].append(ele)
    dotted_dict = copy.deepcopy(sorted_dict)
    for i in dotted_dict.keys():
        for j in range(len(dotted_dict[i])):
            dotted_dict[i][j] = re.sub(r'[a-z]', '-', dotted_dict[i][j])
    return sorted_dict, dotted_dict

word_dict = dict_tuple()
word = choose_word()
my_words = set()
word_lengths, my_words = process_dict(my_words)
sorted_words, dotted_words = dotted_list(my_words, word_lengths)
get_user()
choose_word()
