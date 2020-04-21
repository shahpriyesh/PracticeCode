from collections import Counter

class FindLuckyInteger:
    def findLuckyInteger(self, arr):
        res = -1
        for k, v in Counter(arr).items():
            if k == v:
                res = max(res, v)
        return res


object = FindLuckyInteger()
print(object.findLuckyInteger([2,2,3,4]))
print(object.findLuckyInteger([1,2,2,3,3,3]))
print(object.findLuckyInteger([2,2,2,3,3]))
print(object.findLuckyInteger([5]))
print(object.findLuckyInteger([7,7,7,7,7,7,7]))
