from collections import deque

class Solution:
    def RemoveKDigits(self, num, k):
        if k == 0:
            return num
        if len(num) == k:
            return "0"

        stack = []
        i = 0

        while i < len(num):
            # Remove all digits that are greater than current digit.
            # These digits are sure candidates to be removed.
            while k > 0 and len(stack) > 0 and stack[-1] > num[i]:
                stack.pop()
                k -= 1

            stack.append(num[i])
            i += 1

        # For special case where all digits are same Ex. "1111",
        while k > 0:
            stack.pop()
            k -= 1

        # Remove leading zeroes if any
        while stack and stack[0] == "0":
            stack.pop(0)

        return ''.join(stack) if stack else "0"

    def RemoveKDigits_INCORRECT(self, num, k):
        if k == 0:
            return num
        if len(num) == k:
            return "0"

        num = deque(num)
        queue = deque()

        while k > 0:
            queue.append(num.popleft())
            k -= 1

        while queue[0] < num[0]:
            queue.append(num.popleft())
            num.appendleft(queue.popleft())

        # Remove leading zeroes if any
        while num and num[0] == "0":
            num.popleft()

        return ''.join(num) if num else "0"


object = Solution()
print(object.RemoveKDigits("1432219", 3))
print(object.RemoveKDigits("10200", 1))
print(object.RemoveKDigits("10", 2))
print(object.RemoveKDigits("329765", 3))

# This was returning "" as at return we had to check if num has anything left in it
print(object.RemoveKDigits("10", 1))

# This failed because not handling k=0
print(object.RemoveKDigits("0", 0))

# This fails because we don't check equal in queue and num. If we check than it will go in infinite loop
print(object.RemoveKDigits("112", 1))
