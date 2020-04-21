from collections import Counter

class Solution:
    def groupAnagrams(self, strs):
        hmap = {}
        for strng in strs:
            cnt = str(sorted(strng))
            if cnt not in hmap:
                hmap[cnt] = [strng]
            else:
                hmap[cnt].append(strng)

        return hmap.values()


object = Solution()
print(object.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))