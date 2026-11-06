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


            current = current.next

        return False
             
