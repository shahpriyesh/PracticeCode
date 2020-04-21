import collections

class LargestUniqueNumber:
    def largestUniqueNumber(self, nums):
        res = [k for k, v in collections.Counter(nums).items() if v == 1]
        return max(res) if res else -1


object = LargestUniqueNumber()
print(object.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(object.largestUniqueNumber([9,9,8,8]))