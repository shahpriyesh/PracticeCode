import collections

class RelativeSortArray:
    def relativeSortArray(self, arr1, arr2):
        counter = collections.Counter(arr1)
        res = []

        for num in arr2:
            numlist = [num]*counter[num]
            res.extend(numlist)
            del counter[num]

        for k in sorted(counter.keys()):
            res.extend([k]*counter[k])
        return res


object = RelativeSortArray()
print(object.relativeSortArray([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6]))