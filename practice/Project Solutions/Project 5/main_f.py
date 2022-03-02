'''
Project: Project 5 Phileas Fogg (instructor pointer/linked version)
Author: George Rudolph
Course: CS 2420 Fall 2020
Date: 22 Jun 2021

Description: Example main() code that solves the letter frequency project.
This was also used to determine expected results for test cases.
'''
from pathlib import Path
from string import whitespace, punctuation
from bst_f import *


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Relational methods make this object comparable
    using built-in operators.
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'

def make_tree():
    ''' A helper function to build the tree '''
    fname = "around-the-world-in-80-days-3.txt"
    fin = open(fname)
    text = fin.read()
    fin.close()

    bst = BST()
    for ch in text:
        if ch in whitespace + punctuation:
            continue
        try:
            pair = find(bst, Pair(ch))
            pair.count +=1
        except ValueError:
            entry = Pair(ch, 1)
            bst = add(bst,entry)
        #print(bst)
        #print()
    return bst

def main():
    bst = make_tree()

    print("bst in main")
    print(bst)
    print("pre:" , preorder(bst)[27])
    print("in:" , inorder(bst)[27])
    print("post:" , postorder(bst)[27])
    print(size(bst))
    print(height(bst))

    for f in [preorder, inorder, postorder]:
        print(f(bst))

if __name__ == "__main__":
    main()
