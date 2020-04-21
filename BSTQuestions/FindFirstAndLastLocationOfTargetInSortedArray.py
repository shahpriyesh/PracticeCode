class Solution:
    def findFirstAndLastLocation(self, nums, target):
        if not nums:
            return [-1, -1]

        first = last = self.binarySearch(nums, target, 0, len(nums)-1)
        res = [first, last]

        while first != -1:
            first = self.binarySearch(nums, target, 0, first-1)
            if first != -1:
                res[0] = first

        while last != -1:
            last = self.binarySearch(nums, target, last+1, len(nums)-1)
            if last != -1:
                res[1] = last

        return res

    def binarySearch(self, nums, target, start, end):
        if start > end:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binarySearch(nums, target, start, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, end)


object = Solution()
print(object.findFirstAndLastLocation([5,7,7,8,8,10], 8))
print(object.findFirstAndLastLocation([5,7,7,8,8,10], 6))
print(object.findFirstAndLastLocation([], 0))
print(object.findFirstAndLastLocation([1], 1))