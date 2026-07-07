class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverse(head):

    while head:
        print(head.data,end=" -> ")
        head = head.next
    print('Null')


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)

# node1.next = node2
# node2.next = node3

# print(traverse(node1))




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

# node1 = Node(7)
# node2 = Node(11)
# node3 = Node(3)
# node4 = Node(2)
# node5 = Node(9)

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print(find_lowest_val(node1))




# delete node from a linked list
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def delete(self,key):
        temp = self.head 

        if (temp is not None): 
            if (temp.val == key): 
                self.head = temp.next
                temp = None
                return
        while(temp is not None): 
            if temp.val == key: 
                break
            prev = temp 
            temp = temp.next

        if(temp == None): 
            return

        prev.next = temp.next
        temp = None
    
    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp= temp.next
        print("None")
llist = linkedlist()
llist.push(7)
llist.push(3)
llist.push(1)
llist.push(2)

llist.printLinkedList()
llist.delete(1)
print("\n")
llist.printLinkedList()

print("\n")

        