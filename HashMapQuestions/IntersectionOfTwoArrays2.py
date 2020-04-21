import collections

class IntersectionOfTwoArrays2:
    def intersection(self, nums1, nums2):
        return list((collections.Counter(nums1) & collections.Counter(nums2)).elements())


object = IntersectionOfTwoArrays2()
print(object.intersection([1,2,2,1], [2,2]))
print(object.intersection([4,9,5], [9,4,9,8,4]))