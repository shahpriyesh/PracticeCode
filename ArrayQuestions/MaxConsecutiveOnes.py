class MaxConsecutiveOnes:
    def maxConsecutiveOnes(self, nums):
        max_ones = 0
        ones = 0
        for num in nums:
            if num:
                ones += 1
            else:
                max_ones = max(max_ones, ones)
                ones = 0
        max_ones = max(max_ones, ones)
        return max_ones


object = MaxConsecutiveOnes()
print(object.maxConsecutiveOnes([1,1,0,1,1,1]))