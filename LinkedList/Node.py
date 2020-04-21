class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def getVal(self):
        return self.val

    def setVal(self, val):
        self.val = val

    def getNext(self):
        return self.next

    def setNext(self, next):
        self.next = next