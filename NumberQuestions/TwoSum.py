class TwoSum:
    def __init__(self):
        pass

    def twoSum(self, nums, target):
        if len(nums) < 2:
            return []

        dict = {}
        for idx in range(len(nums)):
            if nums[idx] in dict:
                return [dict[nums[idx]], idx]
            else:
                dict[target - nums[idx]] = idx

        return []


object = TwoSum()
A = [2, 7, 11, 15]
print(object.twoSum(A, 18))