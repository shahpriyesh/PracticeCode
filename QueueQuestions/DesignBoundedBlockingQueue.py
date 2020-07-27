from threading import Condition
from collections import deque


class BoundedBlockingQueue(object):

    def __init__(self, capacity):
        self.q = deque()
        self.capacity = capacity
        self.qsize = 0
        self.mutex = Condition()

    def enqueue(self, element):
        self.mutex.acquire()

        if self.qsize >= self.capacity:
            self.mutex.wait()

        self.q.appendleft(element)
        self.qsize += 1

        self.mutex.notify()

        self.mutex.release()

    def dequeue(self):
        self.mutex.acquire()

        if self.qsize <= 0:
            self.mutex.wait()

        res = self.q.pop()
        self.qsize -= 1

        self.mutex.notify()

        self.mutex.release()

    def size(self):
        self.mutex.acquire()
        s = self.qsize
        self.mutex.release()
        return s


object = BoundedBlockingQueue(2)
print(object.enqueue(1))
print(object.dequeue())
print(object.dequeue())
print(object.enqueue(0))
print(object.enqueue(2))
print(object.enqueue(3))
print(object.enqueue(4))
print(object.dequeue())
