from collections import Counter

class Solution:
    def findUncommon(self, A, B):
        cntr_a = Counter(A.split())
        cntr_b = Counter(B.split())

        res = []
        res.extend(self._retrieveUncommon(cntr_a, cntr_b))
        res.extend(self._retrieveUncommon(cntr_b, cntr_a))
        return res

    def _retrieveUncommon(self, cntr1, cntr2):
        res = []
        for item, cnt in cntr1.items():
            if cnt == 1:
                if item not in cntr2:
                    res.append(item)
        return res


object = Solution()
A = "this apple is sweet"
B = "this apple is sour"
print(object.findUncommon(A, B))
A = "apple apple"
B = "banana"
print(object.findUncommon(A, B))