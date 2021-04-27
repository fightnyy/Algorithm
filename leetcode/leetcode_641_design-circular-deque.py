class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = collections.deque()
        self.size = k
        self.front = 0
        self.end = 0

        """
        Initialize your data structure here. Set the size of the deque to be k.
        """

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) >= self.size:
            return False
        else:
            self.deque.appendleft(value)
            return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) >= self.size:
            return False
        else:
            self.deque.append(value)
            return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == 0:
            return False
        else:
            self.deque.popleft()
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if len(self.deque) == 0:
            return False
        else:
            self.deque.pop()
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if len(self.deque) == 0:
            return -1
        else:
            return self.deque[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        if len(self.deque) == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        if len(self.deque) == self.size:
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
