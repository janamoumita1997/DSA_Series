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
