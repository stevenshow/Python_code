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

low_high = re.sub(r'\D', '', input('Enter the range of word lengths (low,high): '))
low = int(low_high[0])
high = int(low_high[1:])

def get_user():
    if(shuffled_word == word):
        shuffle()
    else:
        print(shuffled_word + ':')
    guess = input('Enter a guess: ')
    
    

def shuffle():
    '''Shuffles the word each time that the user guesses a word'''
    word_list = list(word)
    random.shuffle(word_list)
    shuffled_word = ''.join(word_list)
    return(shuffled_word)

def choose_word():
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

def process_dict(guess_list):
    '''Scrambles chosen word and creates subset of all words of length
    low->high-1'''
    word_lengths = set()
    guess_list = set()
    for i in range(low, high):
        #words are not fully scrambling for every combination
        letter_tuples = list(combinations(word, i))
        my_words = [''.join(tups) for tups in letter_tuples]
        get_extra_words(my_words, guess_list, word_lengths)
    return(word_lengths, guess_list)

def get_extra_words(my_words, guess_list, word_lengths):
    '''Helper function for process_dict() to place words into list'''
    for word in my_words:
        if (word[0], len(word)) in word_dict:
            if word in word_dict[(word[0], len(word))]:   
                guess_list.add(word)
                word_lengths.add(len(word))

def dotted_list():
    sorted_words = sorted(list(my_words))
    #print(sorted_words)
    sorted_dict = {}
    for word in sorted_words:
        if len(word) in sorted_dict:
            sorted_dict[len(word)].append(word)
        else:
            sorted_dict[len(word)] = [word]
    dotted_dict = sorted_dict.copy()
    for i in dotted_dict.keys():
        for j in range(len(dotted_dict[i])):
            dotted_dict[i][j] = re.sub(r'[a-z]', '-', dotted_dict[i][j])
    print(dotted_dict)
    return((sorted_dict))

word_dict = dict_tuple()
word = choose_word()
my_words = set()
shuffled_word = shuffle()
word_lengths, my_words = process_dict(my_words)
sorted_words = dotted_list()

#print(my_words)
#print(word_lengths)

get_user()
choose_word()
dotted_list()

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
