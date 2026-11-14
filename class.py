class Node:
    def __init__(self,data):
        self.data = data
        self.next = None




node1 = Node("Me")
node2 = Node("Yo")
node3 = Node(7)
node4 = Node(9)
node5 = Node(11)

head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5


def traveerse_linked_list(head):
    currentNode = head
    while currentNode is not None:
        print(currentNode.data, end = " -> ")
        currentNode = currentNode.next
    print("null")
    
def insert_at_beginning(head, new_data):
    new_node = Node(new_data)
    new_node.next = head
    head = new_node 
    return head

 