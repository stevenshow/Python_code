# getSize() - Get the number of items in the stack
# isEmpty() - Return True if the stack is empty, False otherwise
# peek() - Return the top item in the stack. If the stack is empty, raise an exception
# push(a) - Inserts the element 'a' at the top of the stack
# pop() - Deletes the topmost element of the stack

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node('head')
        self.size = 0
    
    def __str__(self):
        cur = self.head.next
        output = ''
        while cur:
            output += str(cur.value) + '->'
            cur = cur.next
        return output[:-2]

    def getSize(self):
        return self.size

    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEmpty():
            raise Exception('Can\'t peek, Stack is empty!')
        return self.head.next.value
    
    def push(self, a):
        node = Node(a)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.isEmpty():
            raise Exception('Can\'t pop, Stack is empty!')
        to_delete = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return to_delete.value

class main():
    stack = Stack()
    for i in range(1,10):
        stack.push(i)
    print(stack)
    for i in range(0,4):
        print(f'Popped: {stack.pop()}')
    print(stack)
    

if __name__ == '__main__':
    main()