class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        finalPtr = finalHead = ListNode(0)
        ptr1 = head
        # keep dummyHead to construct partial list
        dummyHead = ListNode(0)
        dummyPtr = dummyHead
        count = 0
        while ptr1:
            # construct new list of k nodes
            dummyPtr.next = ListNode(ptr1.val)
            # keep count
            count += 1
            # k nodes found?
            if count == k:
                # reverse k nodes and append in final list
                finalPtr.next = self.reverse(dummyHead.next)
                # move till end of list so that new list can be appended
                while finalPtr.next:
                    finalPtr = finalPtr.next
                # reset dummy head
                dummyHead = ListNode(0)
                dummyPtr = dummyHead
                count = 0
            else:
                dummyPtr = dummyPtr.next
            # move to next node
            ptr1 = ptr1.next
        # append remaining nodes
        finalPtr.next = dummyHead.next
        return finalHead.next

    def reverse(self, head) -> ListNode:
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev


head = ListNode(1)
ptr = head
ptr.next = ListNode(2)
ptr = ptr.next
ptr.next = ListNode(3)
ptr = ptr.next
ptr.next = ListNode(4)
ptr = ptr.next
ptr.next = ListNode(5)
ptr = ptr.next
object = Solution()
result = object.reverseKGroup(head, 2)
while result:
    print(result.val, end="-> ")
    result = result.next

print()
result = object.reverseKGroup(head, 3)
while result:
    print(result.val, end="-> ")
    result = result.next