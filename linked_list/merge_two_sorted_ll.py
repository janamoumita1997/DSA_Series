from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1:Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode()
    curr = head

    if not 