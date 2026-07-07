from typing import Optional

class Node:
    def __init__(self,val:int = 0, next:Optional['Node'] = None):
        self.val = val
        self.next = next
    
class Solution:
    def middleNode(self, head:Optional['Node']) -> Optional['Node']:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

def create_linkedlist(arr:list[int]) -> Optional['Node']:
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for i in arr[1:]:
        current.next = Node(i)
        current = current.next
    return head

def linkedlist_to_list(head: Optional['Node']) -> list:
    res = []

    while head:
        res.append(head.val)
        head = head.next
    return res


head = [1,2,3,4,5]
head_1 = create_linkedlist(head)
solution = Solution()
middle_node_1 = solution.middleNode(head_1)
print(linkedlist_to_list(middle_node_1))
