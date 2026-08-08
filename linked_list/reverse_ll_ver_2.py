from typing import Optional
class ListNode:
    def __init__(self, val:int = 0, next:Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional['ListNode'], left:int, right:int):
        if not head or left ==right:
            return head
        # place the prev before left node
        dummy = ListNode(0,head)
        leftPrev, curr = dummy, head
        for i in range(left-1):
            leftPrev,curr = leftPrev.next, curr.next

        # reverse the linked list between left and right
        prev = None
        for i in range(right-left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # Connect with rest of the linkedlist
        leftPrev.next.next = curr
        leftPrev.next = prev

        # return head
        return dummy.next
