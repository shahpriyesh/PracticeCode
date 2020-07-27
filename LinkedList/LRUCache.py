class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cnt = 0
        self.head = None

    def get(self, key):
        if not self.head:
            return -1
        curr = self.head
        while curr and curr.val != key:
            curr = curr.next

        if not curr:
            return -1

        # move the node to front
        temp = curr
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        curr_head = self.head
        curr_head.prev.next = curr
        curr_head.prev = curr
        self.head = curr

        return curr.val

    def put(self, key, value):
        if not self.head:
            self.head = Node(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.cnt += 1
            return

        if self.cnt >= self.capacity:
            # remove least recently used entry from end of list
            candidate = self.head.prev
            self.head.prev = candidate.prev
            candidate.prev.next = self.head
