class MinimumAbsoluteDifference:
    def minAbsDiff(self, arr):
        if len(arr) < 2:
            return []

        arr.sort()
        min_diff = float('inf')

        for i in range(len(arr)-1):
            min_diff = min(min_diff, arr[i+1] - arr[i])

        return [[arr[i], arr[i+1]] for i in range(len(arr)-1) if arr[i+1] - arr[i] == min_diff]


object = MinimumAbsoluteDifference()
print(object.minAbsDiff([4,2,1,3]))
print(object.minAbsDiff([1,3,6,10,15]))
print(object.minAbsDiff([3,8,-10,23,19,-4,-14,27]))