class Node:
    def _init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

    def display(self):
        current  = self.head

        while current is not None:
            print(current.data, end = " -> ")
            current = current.next

        print("None")

    def search(self,data):
        current = self.head

        while current is not None:
            if current.data == value:
                return True



    class Node:
    def __init__(self,data):


class LinkedInList:
    def __init__(self,data):
        self.data = data
        self.next = None

    def insert_in_linkedlist(head, new_data):
        new_node = Node(new_data)
        new_node.next = head
        head = new_node
        return head

    def remove_from_linkedlist(head, del_data):
        if del_data == 0:
            return head.next
        node = head
        for d in range(del_data - 1):
            node = node.next
        node.next = node.next.next
        return head

    def find_in_linkedlist(head, find_data):
        if find_data == head:
            return head

        
        for i in range(find_data - 1):





class Node:
    def __init__(self, data):
        self.data = data#initializes data
        self.next = None#points to next node which is none


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return "added"

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current != None:
            print(current.data)
            current = current.next
        print("Done traversing")

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def search(self, target):
        current = self.head
        while current != None:
            if current.data == target:
                return True

            current = current.next
        return False

    def delete(self, target):
        if self.head == None:
            return "List is empty"
        
        if self.head.data == target:
            self.head = self.head.next
            return "Deleted"

        previous = self.head
        current = self.head.next

        while current != None:
            if current.data == target:
                previous.next = current.next
            return "Deleted"

        previous = current 
        current = current.next

        return "Value not found"



students = LinkedList()

students.insert_end(1001)
students.insert_end(1002)
students.insert_end(1003)
students.insert_end(1004)
students.insert_end(1005)

students.display()

def insert_beginning(self, data):
    new_node = Node(data)
    new_node.next = self.head
    self.head = new_node

def insert_end(self, data):
    new_node = Node(data)

    if self.head == None:
        self.head = new_node
        return "added"

    current = self.head
    while current.next != None:
        current = current.next
    current.next = new_node


stud = LinkedList()

stud.insert_end(10)
stud.insert_end(20)

def search(self, target):
    current = self.head

    while current != None:
        if current.data == target:
            return True

        current = current.next

    return False

def delete(self, target):
    if self.head == None:
        return "List is empty"

    if self.head.data == target:
        self.head = self.head.next
        return "Deleted"

    previous = self.head
    current = self.head.next

    while current != None:
        if current.data == target:
            previous.next = current.next
            return "Deleted"

        previous = current
        current = current.next

    return "value not found"

stud.delete(20)

stud.display()

def search(self, target):
    current = self.head

    while current != None:
        if current.data == target:
            return True
        current = current.next
    return False


            



            current = current.next

        return False
             



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return "added"

        current= self.head

        while current.next != None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current != None:
            print(current.data,", ")
            current = current.next


    def search(self, target):
        if self.head.data == target:
            return True

        current = self.head

        while current != None:
            if current.data == target:
                print("Value found..")
            current = current.next
        return False

    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        current = self.head

        if self.head == None:
            self.head = new_node
            return "done"

        while current.next != None:
            current = current.next
        current.next = new_node

###STACKS
#push()- adds to stack
#pop()- removes from stack
#peek() - view the top element
#isEmpty() - check whether the stack is empty

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack[-1])

if len(stack) == 0:
    print("Tis wmpty")
else:
    print("Stack is not empty")


class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)

    def  pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        
        return self.stack[-1]





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return "added"

        current= self.head

        while current.next != None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current != None:
            print(current.data,", ")
            current = current.next


    def search(self, target):
        if self.head.data == target:
            return True

        current = self.head

        while current != None:
            if current.data == target:
                print("Value found..")
            current = current.next
        return False

    def insert_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        current = self.head

        if self.head == None:
            self.head = new_node
            return "done"

        while current.next != None:
            current = current.next
        current.next = new_node

###STACKS
#push()- adds to stack
#pop()- removes from stack
#peek() - view the top element
#isEmpty() - check whether the stack is empty

stack = []

stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

stack.pop()

print(stack[-1])

if len(stack) == 0:
    print("Tis wmpty")
else:
    print("Stack is not empty")


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack is empty"

        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is emptyyy."

        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True 
        else:
            return False


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return "Tis is empty"

        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            return "Thy stack is empty"

        return self.stack[-1]

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False


#with stack overflow and underflow
class Stack:
    def __init__(self, capacity):
        self.stack = []
        self.capacity = capacity

    def push(self, data):
        if len(self.stack) == self.capacity:
            return "Stack Overflow"

        self.stack.append(data)

    def pop(self):
        if len(self.stack) == 0:
            return "Stack Underflow"

        return self.stack.pop()




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def preOrderTraversal(node):
        if node == None:
            return 
        print(node.data, end=", ")
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)

class stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def push(self, data):
        if self.top == self.capacity - 1:
            return "Stack Overflow."

        self.top += 1

        self.stack[self.top] = data

    def pop(self):
        if self.top == - 1:
            return "Stack Underflow"

        popped = self.stack[self.top]

        self.top -= 1

        return popped

    def peek(self):
        if self.top == - 1:
            return "Stack Underflow"

        return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
