class MissingRanges:
    def missingRanges(self, nums, lower, upper):
        prev = lower
        res = []
        for num in nums:
            if num - prev == 2:
                res.append(str(num-1))
            elif num - prev > 2:
                res.append(str(prev+1) + "->" + str(num-1))
            prev = num

        if upper - prev > 1:
            res.append(str(prev+1) + "->" + str(upper))

        return res


object = MissingRanges()
nums = [0, 1, 3, 50, 75]
print(object.missingRanges(nums, 0, 99))