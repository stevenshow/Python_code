'''
:Project Name: Phileas Fogg Has a Hgh-Stakes Conversation (instructor linked/pointer version)
:Author: George Rudolph
:Date: 22 Jun 2021

Implement a binary search tree that reads text from a file and stores letter
frequency counts.

'''

class Node:
    ''' Defines the Node of the BinarySearchTree '''
    def __init__(self, data, left_child=None, right_child=None):
        ''' initialized a Node '''
        self.data = data
        self.left = left_child
        self.right = right_child

    def is_leaf(self):
        ''' returns True if Node has not children, else returns False '''
        return not self.left and not self.right

    def __str__(self):
        ''' returns a string representation of the Node '''
        return f"Node({self.data})"

class BST:
    ''' defines a Binary Search Tree data structure '''
    def __init__(self):
        ''' initialized the tree as empty '''
        self.root = None

    def is_empty(self):
        ''' returns True if the tree is empty, else False '''
        return self.root is None

    def add(self, data):
        ''' add a new element (which contains data) to the tree '''

        def add_helper(cursor, data):
            if cursor is None:
                return Node(data)

            if data < cursor.data:
                cursor.left = add_helper(cursor.left, data)
            else:
                cursor.right = add_helper(cursor.right, data)

            return cursor

        self.root = add_helper(self.root, data)

    def find(self, data):
        ''' returns a reference to the Node containing "data".
         if not found, raises a ValueError '''

        def find_helper(cursor, data):
            if cursor is None:
                raise ValueError("Item not found.")

            if cursor.data == data:
                return cursor

            if data < cursor.data:
                return find_helper(cursor.left, data)

            return find_helper(cursor.right, data)

        return find_helper(self.root, data)


    def remove(self, data):
        ''' removes a single Node which contains "data" if found in the tree. '''

        def remove_helper(cursor, data):
            if cursor is None:
                raise ValueError("Not found.")

            if cursor.data == data:
                # case 1: 0 children
                if cursor.is_leaf():
                    return None

                #case 2: only one child
                if cursor.right is None:
                    return cursor.left
                if cursor.left is None:
                    return cursor.right

                # case 3, two children, so find the successor
                # go right once then left as far as possible
                succsessor = cursor.right
                while succsessor.left is not None:
                    succsessor = succsessor.left

                cursor.data = succsessor.data
                #recursively delete the successor node
                cursor.right = remove_helper(cursor.right, succsessor.data)
                return cursor

            #recursive case
            if data < cursor.data:
                cursor.left = remove_helper(cursor.left, data)
            else:
                cursor.right = remove_helper(cursor.right, data)

            return cursor

        self.root = remove_helper(self.root, data)


    def size(self):
        ''' returns the number of Nodes in the tree '''

        def size_helper(cursor):
            if cursor is None:
                return 0
            return 1 + size_helper(cursor.left) + size_helper(cursor.right)

        return size_helper(self.root)


    def preorder(self):
        ''' returns a list of the data in the tree in pre-order '''

        def preorder_helper(cursor, output):
            '''
            if cursor is None:
                print(cursor)
            else: print(cursor.data)
            '''
            if cursor is None:
                return

            output.append(cursor.data)
            if cursor.left:
                preorder_helper(cursor.left, output)
            if cursor.right:
                preorder_helper(cursor.right, output)

        output = []
        preorder_helper(self.root, output)
        return output


    def inorder(self):
        ''' returns an inorder traversal of tree as a list '''

        def inorder_helper(cursor, output):
            '''
            if cursor is None:
                print(cursor)
            else: print(cursor.data)
            '''
            if cursor is None:
                return

            if cursor.left:
                inorder_helper(cursor.left, output)

            output.append(cursor.data)

            if cursor.right:
                inorder_helper(cursor.right, output)

        output = []
        inorder_helper(self.root, output)
        return output

    def postorder(self):
        ''' returns an inorder traversal of tree as a list '''

        def postorder_helper(cursor, output):
            '''
            if cursor is None:
                print(cursor)
            else: print(cursor.data)
            '''
            if cursor is None:
                return

            if cursor.left:
                postorder_helper(cursor.left, output)
            if cursor.right:
                postorder_helper(cursor.right, output)
            output.append(cursor.data)

        output = []
        postorder_helper(self.root, output)
        return output


    def height(self):
        ''' returns the height of the tree '''
        def hop_helper(node):
            if node is None:
                return 0
            return 1 + max(hop_helper(node.right), hop_helper(node.left))

        return hop_helper(self.root)

    def rebalance(self):
        ''' performs a rebalance of the tree '''

        def rebalance_helper(data):
            #base case
            if not data:
                return None

            if len(data) == 1:
                cursor = Node(data[0])
                return cursor

            mid = len(data) // 2
            cursor = Node(data[mid])

            # recursively make the left sub tree and attach it as the left child of cursor
            cursor.left = rebalance_helper(data[:mid])
            cursor.right = rebalance_helper(data[mid:])
            return cursor

        # get an inorder list of the tree
        items = list(self.inorder())
        self.root = rebalance_helper(items)
        return self
