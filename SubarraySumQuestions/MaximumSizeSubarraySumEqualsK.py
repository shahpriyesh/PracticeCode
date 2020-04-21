class MaximumSizeSubarraySumEqualsK:
    def maxSizeSubarraySumEqualsK(self, arr, k):
        max_len = 0
        arr.sort()
        P = [0]*(len(arr)+1)
        for i in range(len(arr)):
            P[i+1] = P[i] + arr[i]

        left, right = 0, 1
        while left < right < len(arr):
            if P[right] - P[left] == k:
                max_len = max(max_len, right - left)
                left += 1
            elif P[right] - P[left] < k:
                right += 1
            elif P[right] - P[left] > k:
                left += 1
        return max_len


object = MaximumSizeSubarraySumEqualsK()
print(object.maxSizeSubarraySumEqualsK([10, 5, 2, 7, 1, 9], 15))
print(object.maxSizeSubarraySumEqualsK([-5, 8, -14, 2, 4, 12], -5))