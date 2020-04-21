import collections


class LongestWordInDictionaryThroughDeleting:
    def longestWordInDictionaryThroughDeleting(self, s, d):
        s_dict = collections.Counter(s)
        d.sort()
        d.sort(key=len, reverse=True)
        for word in d:
            w_dict = collections.Counter(word)
            common = s_dict & w_dict
            if common == w_dict:
                if self.isMatch(s, word):
                    return word
        return ""

    def isMatch(self, s, word):
        ptr1, ptr2 = 0, 0
        while ptr1 < len(s) and ptr2 < len(word):
            if s[ptr1] == word[ptr2]:
                ptr1 += 1
                ptr2 += 1
            else:
                ptr1 += 1
        return ptr2 == len(word)


object = LongestWordInDictionaryThroughDeleting()
print(object.longestWordInDictionaryThroughDeleting("abpcplea", ["ale","apple","monkey","plea"]))
print(object.longestWordInDictionaryThroughDeleting("bab", ["ba","ab","a","b"]))
s = "aewfafwafjlwajflwajflwafj"
d = ["apple","ewaf","awefawfwaf","awef","awefe","ewafeffewafewf"]
print(object.longestWordInDictionaryThroughDeleting(s, d))