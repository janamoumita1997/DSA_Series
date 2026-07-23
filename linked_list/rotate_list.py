from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    first = head
    second = head
    dummy = head
    if not head or not head.next or k==0:
        return head
    length = 0
    while dummy:
        dummy = dummy.next
        length += 1

    effective_k = k%length

    if effective_k == 0:
        return head
    
    for _ in range(effective_k):
        second = second.next
    
    while second and second.next:
        first = first.next
        second = second.next
    
    second.next = head
    head = first.next
    first.next = None

    return head

    
