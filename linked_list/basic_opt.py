class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):

    while head:
        print(head.data,end=" -> ")
        head = head.next
    print('Null')


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3

print(traverse(node1))


## find lowest node in linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def find_lowest_val(head):
    lowest_val = head.data
    while head.next:
        head = head.next
        if head.data < lowest_val:
            lowest_val = head.data
    return lowest_val

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(find_lowest_val(node1))
