'''
Project: Project 5 Phileas Fogg (instructor pointer/linked version)
Author: George Rudolph
Course: CS 2420 Fall 2020
Date: 31 Oct 2020

Description: Example main() code that solves the letter frequency project.
This was also used to determine expected results for test cases.
'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


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
            item = bst.find(Pair(ch))
            item.data.count +=1
        except ValueError:
            entry = Pair(ch, 1)
            bst.add(entry)

    return bst

def main():
    fname = "around-the-world-in-80-days-3.txt"
    p = Path(fname)
    if p.exists():
        fin = open(fname)
    else:
        print(f'File {fname} does not exist.')
        return

    text = fin.read()
    fin.close()

    bst = BST()
    for ch in text:
        if ch in whitespace + punctuation:
            continue
        try:
            item = bst.find(Pair(ch))
            item.data.count +=1
            #print(f"found {ch}")
        except ValueError:
            entry = Pair(ch, 1)
            bst.add(entry)
            #print(f"new {ch}")

    print("pre:" , bst.preorder()[27])
    print("in:" , bst.inorder()[27])
    print("post:" , bst.postorder()[27])
    print(bst.size())
    print(bst.height())

    for pre, ino, post in zip(bst.preorder(), bst.inorder(), bst.postorder()):
        print(pre,ino,post)


if __name__ == "__main__":
    main()
