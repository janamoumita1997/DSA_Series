# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next 

# class FreqStack:
#     def __init__(self):
#         self.curr = ListNode()
#         self.head = None
#         self.freqCount = {}

#     def getMaxCandidates(self,freqCount):
#         max_val = max(self.freqCount.values())
#         max_candidates = [i for i in self.freqCount if self.freqCount[i]==max_val]
#         return max_candidates

#     def push(self,val:int)-> None:
#         self.head = ListNode(val)
#         self.head.next = self.curr
#         self.curr = self.head

#         self.freqCount[val] = self.freqCount.get(val,0) + 1

#     def pop(self) -> int:
#         possible_candidates = self.getMaxCandidates(self.freqCount)
#         if self.curr.val in possible_candidates:
#             self.freqCount[self.curr.val] = self.freqCount.get(self.curr.val,0) - 1
#             x = self.curr.val
#             self.curr = self.curr.next
#             self.head = self.curr
#         else:
#             while self.curr.next:
#                 if self.curr.next.val in possible_candidates:
#                     self.freqCount[self.curr.next.val] = self.freqCount.get(self.curr.next.val,0) - 1
#                     x = self.curr.next.val
#                     self.curr.next = self.curr.next.next
#                     break
#                 self.curr = self.curr.next
#             self.curr = self.head
#         return x


# class FreqStack:
#     def __init__(self):
#         self.st1 = []
        
#         self.freqCount = {}

#     def getMaxCandidates(self, freqCout):
#         maxVal = max(self.freqCount.values())
#         maxCandidates = [i for i in self.freqCount if self.freqCount[i] == maxVal]
#         return maxCandidates
    
#     def push(self, val) -> None:
#         self.st1.append(val)
#         self.freqCount[val] = self.freqCount.get(val,0) + 1

#     def pop(self) -> int:
#         st2 = []
#         if len(self.st1) == 0:
#             return -1
#         possible_candidates = self.getMaxCandidates(self.freqCount)
#         if self.st1[-1] in possible_candidates:
#             x = self.st1[-1]
#             self.st1.pop()   
#         else:
#             while len(self.st1)>0:
#                 temp = self.st1.pop()
#                 if temp in possible_candidates:
#                     x = temp
#                     break
#                 st2.append(temp)
#             self.st1 = self.st1 + st2[::-1]
#         self.freqCount[x] = self.freqCount.get(x,0) - 1
#         return x
                
# freq = FreqStack()
# freq.push(5)
# freq.push(1)
# freq.push(2)
# freq.push(5)
# freq.push(5)
# freq.push(5)
# freq.push(1)
# freq.push(6)
# freq.push(1)
# freq.push(5)
# for i in range(10):
#     print(freq.pop())

class FreqStack:
    def __init__(self):
        self.freq = {}          # val -> count
        self.group = {}         # count -> stack of vals with that count
        self.maxFreq = 0

    def push(self, val: int) -> None:
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        if f > self.maxFreq:
            self.maxFreq = f
        self.group.setdefault(f, []).append(val)

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if not self.group[self.maxFreq]:
            self.maxFreq -= 1
        return val
