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
            



            current = current.next

        return False
             
