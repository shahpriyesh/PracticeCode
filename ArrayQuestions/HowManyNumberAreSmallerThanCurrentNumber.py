class HowManyNumbersAreSmallerThanCurrentNumber:
    def smallerThanCurrent(self, nums):
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda x: x[0])

        prev = -1
        prev_idx = 0
        res = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i][0] == prev:
                res[nums[i][1]] = prev_idx
            else:
                res[nums[i][1]] = i
                prev_idx = i
            prev = nums[i][0]

        return res


object = HowManyNumbersAreSmallerThanCurrentNumber()
print(object.smallerThanCurrent([8,1,2,2,3]))
print(object.smallerThanCurrent([6,5,4,8]))
print(object.smallerThanCurrent([7,7,7,7]))