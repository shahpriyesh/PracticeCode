class RepeatedSubstringPattern:
    def repeatedSubstringPattern(self, s):
        # observe that for n length string to have repeating pattern, it has to be at most n/2 length
        # double the string, this will repeat pattern at most 4 times
        ss = (s + s)
        # now clip the string to remove first and last character
        ss = ss[1:-1]
        # first char and last char are part of pattern which are now clipped

        # look for ss in str if it exist than the pattern is present
        return ss.find(s) != -1


object = RepeatedSubstringPattern()
print(object.repeatedSubstringPattern("abab"))
print(object.repeatedSubstringPattern("aba"))
print(object.repeatedSubstringPattern("abcabcabcabc"))

print(object.repeatedSubstringPattern("ababba"))
print(object.repeatedSubstringPattern("abaababaab"))
print(object.repeatedSubstringPattern("ababababab"))

print(object.repeatedSubstringPattern("abcabcabcabc"))