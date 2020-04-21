class ContainsDuplicates3:
    def containsDuplicates3(self, nums, k, t):
        for i, num in enumerate(nums):
            end = i+k+1 if i+k+1 < len(nums) else len(nums)
            for j in range(i+1, end):
                if abs(num - nums[j]) <= t:
                    return True
        return False


object = ContainsDuplicates3()
print(object.containsDuplicates3([1,2,3,1], 3, 0))
print(object.containsDuplicates3([1,0,1,1], 1, 2))
print(object.containsDuplicates3([1,5,9,1,5,9], 2, 3))