class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = None

    def get(self, key):
        if not self.head:
            return -1
        curr = self.head
        cnt = 1
        while curr and cnt != key:
            curr = curr.next

        if not curr:
            return -1

        # move the node to front
        temp = curr.prev.next
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
