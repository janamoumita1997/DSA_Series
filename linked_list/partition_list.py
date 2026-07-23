from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    head1 = ListNode()
    curr_1 = head1
    head2 = ListNode()
    curr_2 = head2
    while head:
        if head.val < x:
            curr_1.next = ListNode(head.val)
            curr_1 = curr_1.next
        else:
            curr_2.next = ListNode(head.val)
            curr_2 = curr_2.next
        head = head.next
    curr_1.next = head2.next
    return head1.next