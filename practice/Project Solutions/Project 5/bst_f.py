'''
:Project Name: Phileas Fogg Has a Hgh-Stakes Conversation (instructor linked/pointer version)
:Author: George Rudolph
:Date: 22 Jun 2021

Implement a binary search tree that reads text from a file and stores letter
frequency counts. This is a functional version vs OOP: the first argument
is the tree.

'''

def BST():
    ''' make an empty BST '''
    return []

def root(tree):
    '''return the data at the root '''
    return tree[0]

def first(tree):
    '''Helper function returns data item from the current node of the tree'''
    return tree[0]

def left(tree):
    '''Helper function returns left subtree'''
    return tree[1]

def right(tree):
    '''Helper function returns right subtree'''
    return tree[2]
    
def is_empty(tree):
    ''' returns True if the tree is empty, else False '''
    return not tree

def add(tree, data):
    ''' add a new element (which contains data) to the tree '''

    def add_helper(cursor, data):
        if not cursor:
            return [data,[],[]]

        if data < first(cursor):
            cursor[1] = add_helper(left(cursor), data)
        else:
            cursor[2] = add_helper(right(cursor), data)

        return cursor
    tree = add_helper(tree, data)
    return tree

def find(tree, data):
    ''' returns a reference to the Node containing "data", if found; else raises a ValueError '''

    def find_helper(cursor, data):
        if not cursor:
            raise ValueError("Item not found.")

        if first(cursor) == data:
            return first(cursor)

        if data < first(cursor):
            return find_helper(left(cursor), data)

        return find_helper(right(cursor), data)

    return find_helper(tree, data)


def remove(tree, data):
    ''' removes a single Node which contains "data" if found in the tree. '''

    def remove_helper(cursor, data):
        if not cursor:
            raise ValueError("Not found.")

        if first(cursor) == data:
            # case 1: 0 children
            if is_leaf(cursor):
                return []
            
            #case 2: only one child
            if not right(cursor):
                return left(cursor)
            if not left(cursor):
                return right(cursor)
            
            # case 3, two children, so find the successor
            # go right once then left as far as possible
            successor = right(cursor)
            while left(successor):
                successor = left(successor)

            cursor[0] = successor[0]
            #recursively delete the successor node
            cursor[2] = remove_helper(right(cursor), first(successor))
            return cursor

        #recursive case
        if data < first(cursor):
            cursor[1] = remove_helper(left(cursor), data)
        else:
            cursor[2] = remove_helper(right(cursor), data)

        return cursor

    tree = remove_helper(tree, data)
    return tree


def size(tree):
    ''' returns the number of Nodes in the tree '''

    def size_helper(cursor):
        if not cursor:
            return 0
        return 1 + size_helper(left(cursor)) + size_helper(right(cursor))

    return size_helper(tree)


def preorder(tree):
    ''' returns a list of the data in the tree in pre-order '''

    def preorder_helper(cursor, output):
        ''' helper
        '''
        if not cursor:
            return

        output.append(first(cursor))
        if left(cursor):
            preorder_helper(left(cursor), output)
        if right(cursor):
            preorder_helper(right(cursor), output)

    output = []
    preorder_helper(tree, output)
    return output

def inorder(tree):
    ''' returns an inorder traversal of tree as a list '''

    def inorder_helper(cursor, output):
        ''' helper
        '''
        if not cursor:
            return

        if left(cursor):
            inorder_helper(left(cursor), output)
        output.append(first(cursor))
        if right(cursor):
            inorder_helper(right(cursor), output)

    output = []
    inorder_helper(tree, output)
    return output

def postorder(tree):
    ''' returns an inorder traversal of tree as a list '''

    def postorder_helper(cursor, output):
        ''' helper
        '''
        if not cursor:
            return

        if left(cursor):
            postorder_helper(left(cursor), output)
        if right(cursor):
            postorder_helper(right(cursor), output)
        output.append(first(cursor))
        
    output = []
    postorder_helper(tree, output)
    return output


def is_leaf(tree):
    ''' returns True if root has no children, else returns False '''
    return not left(tree) and not right(tree)


def height(tree):
    ''' returns the height of the tree '''
    def hop_helper(cursor):
        if not cursor:
            return 0
        return 1 + max(hop_helper(right(cursor)), hop_helper(left(cursor)))

    return hop_helper(tree)

def rebalance(tree):
    ''' performs a rebalance of the tree '''
    
    def rebalance_helper(lyst):
        #base case
        if not lyst:
            return []

        if len(lyst) == 1:
            cursor = [lyst[0],[],[]]
            return cursor
            
        mid = len(lyst) // 2
        cursor = [lyst[mid],[],[]]

        cursor[1] = rebalance_helper(lyst[:mid])
        cursor[2] = rebalance_helper(lyst[mid:])
        return cursor

    items = inorder(tree)
    new_tree = rebalance_helper(items)
    return new_tree


        
