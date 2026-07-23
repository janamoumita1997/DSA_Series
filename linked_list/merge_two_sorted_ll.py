from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1:Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    curr = head

    if not l1 and not l2:
        return None
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = ListNode(l1.val)
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = ListNode(l2.val)
            curr = curr.next
            l2 = l2.next
    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return head.next
