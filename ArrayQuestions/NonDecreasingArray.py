# https://leetcode.com/problems/non-decreasing-array/

class NonDecreasingArray:
    def __init__(self):
        pass

    def nonDecreasingArrayCheck(self, nums):
        nums_to_modify = 0
        prev = nums[0]

        for num in nums[1:]:
            if num < prev:
                nums_to_modify += 1
            prev = num

        return True if nums_to_modify < 2 else False


object = NonDecreasingArray()
nums = [4,2,1]
print(object.nonDecreasingArrayCheck(nums))
nums = [3,4,2,3]
print(object.nonDecreasingArrayCheck(nums))