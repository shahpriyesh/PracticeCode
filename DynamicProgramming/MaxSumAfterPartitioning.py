class MaxSumAfterPartitioning:
    def maxSumAfterPartitioning(self, A, K):
        N = len(A)
        dp = [0] * (N + 1)
        for i in range(N):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]

    def failed_attempt_at_maxSumAfterPartitioning(self, A, K):
        idx = 0
        list_len = len(A)
        while idx <= (list_len-K-1):

            # from K+1 numbers, check max from first K numbers and max from last K numbers
            max1 = max(A[idx:idx+K])
            max2 = max(A[idx+1:idx+1+K])

            # add last number in K times maximum number from first K numbers
            num1 = (max1 * K) + A[idx+K]
            # add first number in K times maximum number from last K numbers
            num2 = A[idx] + (max2 * K)

            # based on bigger sum, either change first K numbers in list
            if num1 >= num2:
                A[idx:idx+K] = [max1]*K
                idx += K
            # or change last K numbers in list
            else:
                A[idx+1:idx+K+1] = [max2]*K
                idx += K+1

        # if any numbers are left at tail of of the list, than find maximum number from the tail and use it in total
        if idx < len(A)-1:
            max_at_ending = max(A[idx:list_len])
            A[idx: list_len] = [max_at_ending] * (list_len - idx)

        return sum(A)


object = MaxSumAfterPartitioning()
A = [1,15,7,9,2,5,10]
K = 3

A = [1,4,1,5,7,3,6,1,9,9,3]
K = 4

A = [1,10,11,2]
K = 3
print(object.maxSumAfterPartitioning(A, K))