class stack:
    def __init__(self):
        self.s = []
        self.length = 0

    def push(self, val):
        self.s.append(val)
        self.length += 1

    def pop(self):
        if self.length == 0:
            return -1
        x = self.s.pop()
        self.length -= 1
        return x
    
    def size(self):
        return self.length

    def getTop(self):
        if self.length == 0:
            return -1
        return self.s[-1]


class queue:
    def _init_(self):
        self.s1 = []
        self.s2 = []

    def push(self,val):
        self.s1.append(val)

    def pop(self):
        self.is_transfer_needed()
        return self.s2.pop()

    def peek(self):
        self.is_transfer_needed()
        return self.s2[-1]

    def empty(self):
        return not self.s1 and not self.s2
       
    def is_transfer_needed(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())