from collections import defaultdict

class Solution:
    def groupOfSpecialEquivalentStrings(self, A):
        hmap = defaultdict(list)
        for s in A:
            odd = []
            even = []
            for i, c in enumerate(s):
                if i & 1:
                    odd.append(c)
                else:
                    even.append(c)

            odd = ''.join(sorted(list(set(odd))))
            even = ''.join(sorted(list(set(even))))
            key = odd + even
            hmap[key].append(s)

        biggest = None
        biggest_len = 0
        for v in hmap.values():
            if len(v) > biggest_len:
                biggest_len = len(v)
                biggest = v

        return biggest_len


object = Solution()
print(object.groupOfSpecialEquivalentStrings(["abcd","cdab","cbad","xyzz","zzxy","zzyx"]))
print(object.groupOfSpecialEquivalentStrings(["abc","acb","bac","bca","cab","cba"]))