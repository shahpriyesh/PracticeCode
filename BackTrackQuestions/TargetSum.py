class TargetSum:
    def targetSum(self, nums, S):
        cnt = [0]
        self.util(nums, S, cnt, 0, 0, len(nums))
        return cnt[0]

    def util(self, nums, S, cnt, total, start, end):
        if start == end:
            if total == S:
                cnt[0] += 1
            return

        # try adding
        total += nums[start]
        self.util(nums, S, cnt, total, start+1, end)
        total -= nums[start]

        # try subtracting
        total -= nums[start]
        self.util(nums, S, cnt, total, start+1, end)
        total += nums[start]

        return


object = TargetSum()
print(object.targetSum([1, 1, 1, 1, 1], 3))

# time limit exceeded
print(object.targetSum([33,36,38,40,25,49,1,8,50,13,41,50,29,27,18,25,37,8,0,48], 0))