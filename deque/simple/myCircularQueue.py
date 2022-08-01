# 设计循环队列
# https://leetcode.cn/problems/design-circular-queue/

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k + 1
        self.elements = [0 for _ in range(k + 1)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.elements[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[self.front]

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.elements[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return ((self.rear + 1) % self.capacity) == self.front


s = MyCircularQueue(3)
assert s.enQueue(1)
assert s.enQueue(2)
assert s.enQueue(3)
assert not s.enQueue(4)