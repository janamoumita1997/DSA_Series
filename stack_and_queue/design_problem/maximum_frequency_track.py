class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

class FreqStack:
    def __init__(self):
        self.curr = ListNode()
        self.head = None
        self.freqCount = {}

    def getMaxCandidates(self,freqCount):
        max_val = max(self.freqCount.values())
        max_candidates = [i for i in self.freqCount if self.freqCount[i]==max_val]
        return max_candidates

    def push(self,val:int)-> None:
        self.head = ListNode(val)
        self.head.next = self.curr
        self.curr = self.head

        self.freqCount[val] = self.freqCount.get(val,0) + 1

    def pop(self) -> int:
        possible_candidates = self.getMaxCandidates(self.freqCount)
        if self.curr.val in possible_candidates:
            self.freqCount[self.curr.val] = self.freqCount.get(self.curr.val,0) - 1
            x = self.curr.val
            self.curr = self.curr.next
            self.head = self.curr
        else:
            while self.curr.next:
                if self.curr.next.val in possible_candidates:
                    self.freqCount[self.curr.next.val] = self.freqCount.get(self.curr.next.val,0) - 1
                    x = self.curr.next.val
                    self.curr.next = self.curr.next.next
                    break
                self.curr = self.curr.next
            self.curr = self.head
        return x



