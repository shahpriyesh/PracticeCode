from collections import Counter

class SubarraysWithKDifferentIntegers:
    def subarraysWithKDifferentIntegers_INCOMPLETE(self, A, K):
        hmap = Counter(str(A[0]))
        subarrays = 0
        start, end = 0, 1

        while start <= end < len(A):

            if len(hmap.keys()) == K:
                # we found a subarray
                subarrays += 1

                # shrink the window
                shrink_key = str(A[start])
                hmap.subtract(shrink_key)
                if hmap[shrink_key] == 0:
                    del hmap[shrink_key]
                start += 1
            else:
                # we didn't find subarray, keep expanding
                expand_key = str(A[end])
                hmap.update(expand_key)
                end += 1

        return subarrays


object = SubarraysWithKDifferentIntegers()
#print(object.subarraysWithKDifferentIntegers([1,2,1,2,3], 2))