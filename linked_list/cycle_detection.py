from typing import List,Optional

class Node:
    def __init__(self,data:int = 0, next:Optional['Node'] = None):
        self.data = data
        self.next = next

class Solution:
    def isCycle(self, head : Optional['Node']) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast and fast.next == slow:
                return True
        return False


def createlinkedlist(arr:list[int], pos: int) -> Optional['Node']:
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    cycle = head if pos == 0 else None
    for i,val in enumerate(arr[1:]):
        node = Node(val)
        if i == pos:
            cycle = node
        current.next = node
        current = current.next
    current.next = cycle
    return head

arr = [1,2]
pos = -1

head = createlinkedlist(arr,pos)
ans = Solution().isCycle(head)
print(ans)