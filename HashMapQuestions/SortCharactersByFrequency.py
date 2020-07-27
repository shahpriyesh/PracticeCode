from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        cntr = Counter(s)
        return ''.join([x[0]*x[1] for x in cntr.most_common()])


object = Solution()
print(object.frequencySort("abb"))
print(object.frequencySort("tree"))
print(object.frequencySort("cccaaa"))
print(object.frequencySort("Aabb"))