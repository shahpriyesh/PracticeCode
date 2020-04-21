# https://leetcode.com/problems/first-missing-positive/
class FirstMissingPositive:
    def __init__(self):
        pass

    def firstMissingPositive_BySort(self, nums):
        min_not_present = 1
        nums = sorted(nums)
        prev_num = -1
        for num in nums:
            if num > 0 and num != prev_num:
                if num != min_not_present:
                    return min_not_present
                else:
                    min_not_present += 1
                prev_num = num

        return min_not_present

    def firstMissingPositive_ByPlacement(self, nums):
        N = len(nums)
        res = [0] * N

        for num in nums:
            if num > 0:
                res[num] = num


object = FirstMissingPositive()
nums = [3, 4, -1, 1]
#print(object.firstMissingPositive_BySort(nums))
nums = [7, 8, 9, 11, 12]
#print(object.firstMissingPositive_BySort(nums))
nums = [1, 2, 0]
#print(object.firstMissingPositive_BySort(nums))
nums = [0, 2, 2, 1, 1]
#print(object.firstMissingPositive_BySort(nums))
nums = [1, 1000]
print(object.firstMissingPositive_BySort(nums))