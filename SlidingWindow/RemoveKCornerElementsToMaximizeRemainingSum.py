class Solution:
    def RemoveKCornerElements(self, arr, k):
        left, right = 0, len(arr)-1
        if k > len(arr):
            return 0

        while k:
            if arr[left] <= arr[right]:
                left += 1
            else:
                right -= 1
            k -= 1

        if left <= right:
            return sum(arr[left:right+1])

        return 0


object = Solution()
print(object.RemoveKCornerElements([11, 49, 100, 20, 86, 29, 72], 4))
print(object.RemoveKCornerElements([1, 2, 3, 4, 5, 6, 1], 3))