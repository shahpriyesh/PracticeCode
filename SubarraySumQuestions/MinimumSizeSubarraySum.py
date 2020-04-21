class MinimumSizeSubarraySum:
    def minSizeSubarraySum(self, s, nums):
        left, right = 0, 1
        min_len = float('inf')

        P = [0]*(len(nums)+1)
        for i in range(len(nums)):
            P[i+1] = P[i] + nums[i]

        while len(P) > right > left:
            x = P[right] - P[left]
            if s > x:
                right += 1
            else:
                min_len = min(min_len, right - left)
                left += 1
        return min_len if min_len != float('inf') else 0


object = MinimumSizeSubarraySum()
print(object.minSizeSubarraySum(7, [2,3,1,2,4,3]))