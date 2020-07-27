class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr = self.head
        while curr and index > 0:
            curr = curr.next
            index -= 1
        if curr and index == 0:
            return curr.val
        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        obj = Node(val)
        obj.next = self.head
        self.head = obj

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        obj = Node(val)
        if not self.head:
            self.head = obj
            return

        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = obj

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        prev = None
        curr = self.head
        for i in range(index):
            if curr:
                prev = curr
                curr = curr.next
            else:
                return

        if not prev:
            self.addAtHead(val)
        else:
            obj = Node(val)
            obj.next = curr
            prev.next = obj

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        prev = None
        curr = self.head
        while curr and index:
            prev = curr
            curr = curr.next
            index -= 1

        if index == 0 and curr:
            prev.next = curr.next

    def printList(self):
        curr = self.head
        while curr:
            print(curr.val, end=' ')
            curr = curr.next
        print()

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
obj.addAtHead(7)
obj.printList()
obj.addAtHead(2)
obj.printList()
obj.addAtHead(1)
obj.printList()
obj.addAtIndex(3, 0)
obj.printList()
obj.deleteAtIndex(2)
obj.printList()
obj.addAtHead(6)
obj.printList()
obj.addAtTail(4)
obj.printList()
obj.get(4)
obj.printList()
obj.addAtHead(4)
obj.printList()
obj.addAtIndex(5, 0)
obj.printList()
obj.addAtHead(6)
obj.printList()