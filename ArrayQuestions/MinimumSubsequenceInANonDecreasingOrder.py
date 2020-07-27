class Solution:
    def minSubsequence(self, nums):
        res = []
        sub_sum = 0
        non_sub_sum = sum(nums)
        nums.sort(reverse=True)
        idx = 0
        while sub_sum <= non_sub_sum:
            candidate = nums[idx]
            idx += 1
            res.append(candidate)
            sub_sum += candidate
            non_sub_sum -= candidate
        return res


object = Solution()
print(object.minSubsequence([4,3,10,9,8]))
print(object.minSubsequence([4,4,7,6,7]))
print(object.minSubsequence([6]))