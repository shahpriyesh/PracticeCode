class NextPermutation:
    def nextPermutation(self, nums):
        for k in range(len(nums)-2, -1, -1):
            if nums[k+1] > nums[k]:
                for l in range(len(nums)-1, k, -1):
                    if nums[l] > nums[k]:
                        nums[l], nums[k] = nums[k], nums[l]
                        nums[k+1:] = reversed(nums[k+1:])
                        return nums
        return nums[::-1]


object = NextPermutation()
print(object.nextPermutation([1,2,3]))
print(object.nextPermutation([3,2,1]))
print(object.nextPermutation([1,1,5]))