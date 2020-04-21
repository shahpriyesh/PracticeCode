class ShortestUnsortedContinuousSubarray:
    def shortestUnsortedSubarray(self, nums):
        start, end = -1, -1

        if len(nums) <= 1:
            return 0

        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                start = i
                break

        if start >= 0:
            for i in range(start - 1, -1, -1):
                if nums[i] == nums[start]:
                    start -= 1

        for i in range(len(nums)-1, 0, -1):
            if nums[i] < nums[i-1]:
                end = i
                break

        if end >= 0:
            for i in range(end + 1, len(nums)):
                if nums[i] == nums[end]:
                    end += 1

        return end - start + 1 if start >= 0 and end >= 0 else 0


object = ShortestUnsortedContinuousSubarray()
print(object.shortestUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(object.shortestUnsortedSubarray([1, 2, 3, 4]))
print(object.shortestUnsortedSubarray([1]))
print(object.shortestUnsortedSubarray([1, 3, 2, 2, 2]))
print(object.shortestUnsortedSubarray([1, 2, 4, 5, 3]))