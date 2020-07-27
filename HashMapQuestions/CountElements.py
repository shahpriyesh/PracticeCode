from collections import Counter

class CountElements:
    def countElements(self, nums):
        cntr = Counter(nums)
        total = 0
        for k, v in cntr.items():
            if k+1 in cntr:
                total += v
        return total


object = CountElements()
print(object.countElements([1,2,3]))
print(object.countElements([1,1,3,3,5,5,7,7]))
print(object.countElements([1,3,2,3,5,0]))
print(object.countElements([1,1,2,2]))