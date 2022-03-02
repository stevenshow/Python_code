''' cs2420 Project 4 - Stacks \
    Dana Doggett
    Dec 5, 2019
'''

class Stack:
    ''' implements an ADT Stack '''
    CAPACITY = 1000
    def __init__(self):
        ''' initialize an empty stack '''
        self.data = [None] * Stack.CAPACITY
        self._size = 0

    def push(self, item):
        ''' pushes item onto stack '''
        self.data[self._size] = item
        self._size += 1

    def pop(self):
        ''' removes and returns the top element on the stack '''
        if self._size == 0:
            raise IndexError("stack is empty")

        self._size -= 1
        return self.data[self._size]

    def top(self):
        ''' returns the top element of the stack, but keeps it on the stack '''
        if self._size == 0:
            raise IndexError("stack is empty")

        return self.data[self._size - 1]

    def size(self):
        ''' returns the number of elements currently in the stack '''
        return self._size

    def clear(self):
        ''' clears the contents of the stack '''
        self._size = 0
