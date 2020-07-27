from collections import deque

class SlidingWindowMaximum:
    def slidingWindowMaximum(self, nums, k):
        # This queue maintains indices of elements from biggest to smallest
        qi = deque()

        # insert the first biggest element in first k elements
        for i in range(k):
            while qi and nums[qi[-1]] <= nums[i]:
                qi.pop()

            qi.append(i)

        res = [nums[qi[0]]]

        for i in range(k, len(nums)):
            # Remove indices from front of the deque which fell out of window
            while qi and qi[0] < (i - k + 1):
                qi.popleft()

            # Remove indices from end of deque which have smaller elements than current element
            while qi and nums[qi[-1]] <= nums[i]:
                qi.pop()

            # Insert current element's indice at right of deque
            qi.append(i)

            res.append(nums[qi[0]])

        return res


object = SlidingWindowMaximum()
# print(object.slidingWindowMaximum([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
# print(object.slidingWindowMaximum([8, 5, 10, 7, 9, 4, 15, 12, 90, 13], 4))
# print(object.slidingWindowMaximum([1, -1], 1))
# print(object.slidingWindowMaximum([7, 2, 4], 2))
print(object.slidingWindowMaximum([9,10,9,-7,-4,-8,2,-6], 5))