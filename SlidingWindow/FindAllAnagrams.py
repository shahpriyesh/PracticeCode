from collections import Counter

class FindAllAnagrams:
    def findAllAnagrams(self, s, p):
        p_map = Counter(p)
        res = []
        start, end = 0, 0

        k = len(p)
        s_map = Counter(s[:k])

        if not p_map - s_map:
            res.append(0)

        for i in range(k, len(s)):
            s_map.update(s[i])
            s_map.subtract(s[i-k])

            if not p_map - s_map:
                res.append(i-k+1)

        return res


object = FindAllAnagrams()
print(object.findAllAnagrams("cbaebabacd", "abc"))
print(object.findAllAnagrams("abab", "ab"))