class MovingAverageFromDataStream:
    def __init__(self, k):
        self.queue = []
        self.limit = k
        self.sum = 0

    def next(self, val):
        self.sum += val
        if len(self.queue) == self.limit:
            self.sum -= self.queue.pop(0)
        self.queue.append(val)
        return self.sum / len(self.queue)


object = MovingAverageFromDataStream(3)
print(object.next(1))
print(object.next(10))
print(object.next(3))
print(object.next(5))