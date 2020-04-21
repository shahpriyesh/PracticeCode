class SummaryRanges:
    def summaryRanges(self, nums):
        if not nums:
            return nums

        start = end = nums[0]
        res = []
        for i in range(1, len(nums)):
            if nums[i] == end+1:
                end = nums[i]
            else:
                if start == end:
                    res.append(str(start))
                else:
                    res.append(str(start)+"->"+str(end))
                start = end = nums[i]

        if start == end:
            res.append(str(start))
        else:
            res.append(str(start) + "->" + str(end))

        return res


object = SummaryRanges()
nums = [0,1,2,4,5,7]
print(object.summaryRanges(nums))
nums = [0,2,3,4,6,8,9]
print(object.summaryRanges(nums))
nums = []
print(object.summaryRanges(nums))