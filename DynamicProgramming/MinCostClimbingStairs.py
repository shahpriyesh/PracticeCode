class Solution:
    def MinCostClimbingStairs(self, cost):
        dp = [0]*len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return min(dp[-1], dp[-2])


object = Solution()
print(object.MinCostClimbingStairs([10, 15, 20]))
print(object.MinCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))