from collections import Counter

class Solution:
    def findFirstUnique(self, s):
        cntr = Counter(s)
        for i, c in enumerate(s):
            if cntr[c] == 1:
                return i
        return -1


object = Solution()
print(object.findFirstUnique("leetcode"))
print(object.findFirstUnique("loveleetcode"))
print(object.findFirstUnique("aaa"))