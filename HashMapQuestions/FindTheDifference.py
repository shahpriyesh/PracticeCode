from collections import Counter

class FindTheDifference:
    def findDiff(self, s, t):
        return (Counter(t) - Counter(s)).popitem()[0]


object = FindTheDifference()
print(object.findDiff("abcd", "abcde"))
print(object.findDiff("a", "aa"))