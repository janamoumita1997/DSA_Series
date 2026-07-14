from typing import Optional
class ListNode:
    def __init__(self, val:int = 0, next:Optional['ListNode'] = None) -> Optional['ListNode']:
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self,head:Optional['ListNode']) -> Optional['ListNode']:
        slow: Optional['ListNode'] = head
        fast:Optional['ListNode'] = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                ptr:Optional['ListNode'] = head
                while ptr != slow:
                    ptr = ptr.next
                    slow = slow.next
                return ptr
        return None
