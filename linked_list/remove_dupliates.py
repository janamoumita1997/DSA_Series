from typing import Optional
class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode']=None):
        self.val = val
        self.next = next

class Solution:
    def remove_dupliates(self, head:Optional['ListNode']) -> Optional['ListNode']:
        dummy = ListNode(0,head)
        prev = dummy

        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next

            else:
                prev = prev.next
            head = head.next
        return dummy.next
            