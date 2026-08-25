class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.q = [0]*self.k
        self.front = None
        self.rear = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.rear is None:
            self.front = 0
            self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.k
        self.q[self.rear] = value   
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.rear:
            self.front = None
            self.rear = None
        else:
            self.front = (self.front + 1) % self.k
        return True

    def Front(self) -> int:
        if self.front is None:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear is None:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        if self.front is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.rear is None:
            return False
        return self.front == (self.rear + 1) % self.k