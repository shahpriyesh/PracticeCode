from collections import Counter

class MinimumWindowSubstring:
    def minimumWindowSubstring(self, s, t):
        Tmap = Counter(t)
        matchMap = Counter()

        if len(s) < len(t):
            return ""

        start, end = 0, 0
        minStr = []
        minLen = float('inf')

        while start <= end <= len(s):
            if not Tmap - matchMap:
                if minLen >= (end - start):
                    minStr = list(s[start:end])
                    minLen = len(minStr)
                matchMap.subtract(s[start])
                start += 1
            else:
                if end < len(s):
                    matchMap.update(s[end])
                end += 1

        return ''.join(minStr)


object = MinimumWindowSubstring()
print(object.minimumWindowSubstring("geeksforgeeks", "ork"))
print(object.minimumWindowSubstring("ADOBECODEBANC", "ABC"))
print(object.minimumWindowSubstring("this is a test string", "tist"))