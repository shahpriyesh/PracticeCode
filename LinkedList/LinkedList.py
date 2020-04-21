from Node import Node

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertAtFront(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

    def insertAtEnd(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next is not None:
                curr = curr.next
            curr.next = node

    def length(self):
        size = 0
        curr = self.head
        while curr is not None:
            size = size + 1
            curr = curr.next
        return size

    def popFromFront(self):
        temp = self.head
        if self.head is not None:
            self.head = self.head.next
        return temp

    def popFromEnd(self):
        if self.head is None:
            return None
        elif self.head.next is None:
            temp = self.head
            self.head = None
            return temp
        else:
            curr = self.head
            prev = None
            while curr.next is not None:
                prev = curr
                curr = curr.next
            prev.next = curr.next
            return curr

    def popByValue(self, val):
        if self.head is None:
            return None

        if self.head.val is val:
            temp = self.head
            self.head = self.head.next
            return temp

        prev = None
        curr = self.head
        while curr is not None:
            if curr.val is val:
                prev.next = curr.next
                return curr
            else:
                prev = curr
                curr = curr.next

        return None

    def removeNthFromEnd(self, N):
        if self.length() < N:
            return None
        elif self.length() == N:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            slow_ptr = self.head
            fast_ptr = self.head
            for i in range(N+1):
                fast_ptr = fast_ptr.next

            while fast_ptr is not None:
                fast_ptr = fast_ptr.next
                slow_ptr = slow_ptr.next

            temp = slow_ptr.next
            slow_ptr.next = slow_ptr.next.next
            return temp

    def removeElements(self, val):
        dummy = Node(0)
        dummy.next = self.head

        prev = dummy
        curr = self.head

        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next

    def swapPairs(self):
        curr = self.head

        while curr and curr.next:
            temp = curr.next.next
            curr.next.next = curr

            if self.head == curr:
                self.head = curr.next
            else:
                prev.next = curr.next

            curr.next = temp

            prev = curr
            curr = curr.next

        return self.head

    def printList(self, root):
        while root is not None:
            print(str(root.val) + " -> ", end=" ")
            root = root.next
        print()


object = LinkedList()
object.insertAtEnd(1)
object.insertAtEnd(2)
object.insertAtEnd(3)
object.insertAtEnd(4)
object.insertAtEnd(5)
object.insertAtEnd(6)
print(object.printList(object.head))
#object.popFromEnd()
#print(object.printList(object.head))
#object.popFromFront()
#rint(object.printList(object.head))
#object.popByValue(5)
#print(object.printList(object.head))
#print("Removed : " + str(object.removeNthFromEnd(2).val))
#print(object.printList(object.head))
#curr = object.removeElements(6)
curr = object.swapPairs()

#while curr is not None:
#    print(str(curr.val) + " -> ", " ")
#    curr = curr.next
