from collections import deque

class stack:
    def _init_(self):
        self.q = deque()

    def push(self,x:int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        if len(self.q) == 0:
            return -1
        return self.q.popleft()

    def Top(self):
        if len(self.q) == 0:
            return -1
        return self.q[0]
    def empty(self):
        return len(self.q) == 0