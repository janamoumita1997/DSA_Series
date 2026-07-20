l1 = [2,4,3]
l2 = [5,6,4]
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def add_two_ll(l1,l2):
    head = Optional[ListNode]
    curr = head
    if not l1 and not l2:
        return head
    inhand = 0
    while l1 or l2:
        
        add_val = l1.val if l1 else 0 + l2.val if l2 else 0 + inhand

        
        curr.next = ListNode(int(str(add_val)[-1]))
        curr = curr.next
        inhand = int(str(add_val)[:-1]) if add_val > 9 else 0

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        
    while inhand:
        curr.next = ListNode(int(str(inhand)[-1]))
        curr = curr.next
        inhand = int(str(inhand)[:-1]) if inhand > 9 else 0
    return head
