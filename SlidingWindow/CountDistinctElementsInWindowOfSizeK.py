from collections import Counter

class CountDistinctElementsInWindowOfSizeK:
    def count(self, A, K):
        hmap = Counter(''.join(map(str, A[:K])))
        distinct = len(hmap.keys())

        for i in range(K, len(A)):
            key = str(A[K - i])
            hmap.subtract(key)
            if hmap[key] == 0:
                del hmap[key]
                distinct -= 1

            key = str(A[i])
            hmap.update(key)
            if hmap[key] == 1:
                distinct += 1

        return distinct


object = CountDistinctElementsInWindowOfSizeK()
print(object.count([1, 2, 1, 3, 4, 2, 3], 4))
print(object.count([1, 2, 4, 4], 2))