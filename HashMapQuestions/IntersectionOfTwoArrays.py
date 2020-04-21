import collections

class IntersectionOfTwoArrays:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))


object = IntersectionOfTwoArrays()
print(object.intersection([1,2,2,1], [2,2]))
print(object.intersection([4,9,5], [9,4,9,8,4]))