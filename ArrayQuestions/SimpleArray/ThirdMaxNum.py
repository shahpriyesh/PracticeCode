class ThirdMaxNum:
    def thirdMaxNum(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        x = y = z = float('-inf')
        for num in nums:
            if num > z:
                z = num
            if num > y:
                z = y
                y = num
            if num > x:
                y = x
                x = num
        return z


object = ThirdMaxNum()
print(object.thirdMaxNum([3, 2, 1]))
print(object.thirdMaxNum([1, 2]))
print(object.thirdMaxNum([2, 2, 3, 1]))
print(object.thirdMaxNum([1, 1, 2]))