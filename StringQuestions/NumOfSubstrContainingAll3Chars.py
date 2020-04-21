class NumberOfSubstringsContainingAll3Chars:
    def numberOfSubstrs(self, s):
        res = 0
        first = [-1]*3
        for i in range(len(s)):
            first[ord(s[i]) - ord('a')] = i
            res += (1 + min(first))

        return res


object = NumberOfSubstringsContainingAll3Chars()
print(object.numberOfSubstrs("abcabc"))
print(object.numberOfSubstrs("aaabc"))
print(object.numberOfSubstrs("abc"))
