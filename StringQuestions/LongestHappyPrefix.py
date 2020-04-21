class LongestHappyPrefix:
    def longestHappyPrefix(self, s):
        for x in range(len(s)-1, -1, -1):
            s1 = s[:x]
            s2 = s[len(s)-x:]
            if s1 == s2:
                break
        return s[:x] if x >= 0 else ""


object = LongestHappyPrefix()
print(object.longestHappyPrefix("label"))
print(object.longestHappyPrefix("ababab"))
print(object.longestHappyPrefix("leetcodeleet"))
print(object.longestHappyPrefix("a"))