class MyCircularQueue:
    def __init__(self, k: int):
        self.cqueue = []
        self.size = k

    def enQueue(self, value: int) -> bool:
        if len(self.cqueue) >= self.size:
            return False

        else:
            self.cqueue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.cqueue:
            self.cqueue.pop(0)
            return True

        else:
            return False

    def Front(self) -> int:
        if self.cqueue:
            return self.cqueue[0]
        else:
            return -1

    def Rear(self) -> int:

        if not self.cqueue:
            return -1
        else:
            return self.cqueue[-1]

    def isEmpty(self) -> bool:
        if len(self.cqueue) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:

        if len(self.cqueue) != self.size:
            return False
        else:
            return True


class MyCircularQueue:
    """
    rear은 담을 공간 front는 나갈 공간을 의미한다.
    즉 enqueue 하면 rear에 들어가고
    dequeue 하면 front에 들어간다.
    """

    def __init__(self, k: int):
        self.q = [None] * k
        self.maxlen = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True

        else:
            return False

    def Front(self) -> int:
        return -1 if self.q[self.front] == None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] == None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.q[self.front] == None and self.front == self.rear:
            return True
        else:
            return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.q[self.front] is not None:
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
