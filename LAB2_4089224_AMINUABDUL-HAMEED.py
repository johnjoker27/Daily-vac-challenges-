
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return self.head

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node
        return current.next

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")

    def search(self, value):
        current = self.head

        while current != None:
            if current.data == value:
                return "Value found"

            current = current.next

        return "Value not found"

    def delete(self, target):
        if self.head == None:
            return "This list is empty"

        if self.head.data == target:
            self.head = self.head.next
            return "Target found and removed"

        current = self.head

        while current.next != None:
            if current.next.data == target:
                current.next = current.next.next
                return "Target found and removed"

            current = current.next

        return "Target not found"

    
    def reverse(self):
        previous = None
        current = self.head

        while current != None:
            next_node = current.next
            current.next = previous

            previous = current
            current = next_node

        self.head = previous

    # Find the middle element
    def find_middle(self):
        if self.head == None:
            return "List is empty"

        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow.data



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return

        current = self.head

        while current.next != None:
            current = current.next

        current.next = new_node
        new_node.prev = current

    def display(self):
        current = self.head

        while current != None:
            print(current.data, end=" <--> ")
            current = current.next

        print("None")

    def search(self, value):
        current = self.head

        while current != None:
            if current.data == value:
                return "Value found"

            current = current.next

        return "Value not found"

    def delete(self, target):
        current = self.head

        while current != None:
            if current.data == target:

                if current.prev != None:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next != None:
                    current.next.prev = current.prev

                return "Target found and removed"

            current = current.next

        return "Target not found"



class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def display(self):
        if self.head == None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current == self.head:
                break

        print("(Back to Head)")

    def search(self, value):
        if self.head == None:
            return "Value not found"

        current = self.head

        while True:
            if current.data == value:
                return "Value found"

            current = current.next

            if current == self.head:
                break

        return "Value not found"

    def delete(self, target):
        if self.head == None:
            return "List is empty"

        current = self.head
        previous = None

        while True:

            if current.data == target:

                
                if current.next == self.head and current == self.head:
                    self.head = None
                    return "Target found and removed"

                
                if current == self.head:
                    last = self.head

                    while last.next != self.head:
                        last = last.next

                    self.head = self.head.next
                    last.next = self.head

                else:
                    previous.next = current.next

                return "Target found and removed"

            previous = current
            current = current.next

            if current == self.head:
                break

        return "Target not found"




# Part where i try to test my code that will most definitely make me cry ...... this should not be on the exams pls... i'm begging y'all .... make our lives easier.... chichin.

my_list = LinkedList()

my_list.add(10)
my_list.add(20)
my_list.add(30)
my_list.add(40)
my_list.add(50)

print("SINGLY LINKED LIST")
my_list.display()

print("Search:", my_list.search(30))
print("Delete:", my_list.delete(20))

my_list.display()

print("Middle element:", my_list.find_middle())

my_list.reverse()

print("Reversed list:")
my_list.display()




dll = DoublyLinkedList()

dll.add(10)
dll.add(20)
dll.add(30)

print("\nDOUBLY LINKED LIST")
dll.display()

print(dll.search(20))
print(dll.delete(20))

dll.display()



cll = CircularLinkedList()

cll.add(10)
cll.add(20)
cll.add(30)

print("\nCIRCULAR LINKED LIST")
cll.display()

print(cll.search(20))
print(cll.delete(20))

cll.display()
