class ProductOfArrayExceptSelf:
    def __init__(self):
        pass

    def productOfArrayExceptSelf(self, nums):
        left = [1]*len(nums)
        right = [1]*len(nums)
        multiplier = 1

        left[0] = nums[0]
        right[-1] = nums[-1]

        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i]

        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1]*nums[j]

        size = len(nums)
        nums[0] = right[1]
        nums[-1] = left[-2]
        for k in range(1, len(nums)-1):
            nums[k] = left[k-1]*right[k+1]

        return nums


object = ProductOfArrayExceptSelf()
nums = [1,2,3,4]
print(object.productOfArrayExceptSelf(nums))