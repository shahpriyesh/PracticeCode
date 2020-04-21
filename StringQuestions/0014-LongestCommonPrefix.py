class LongestCommonPrefix:
    def __init__(self):
        pass

    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        sorted(strs)
        len_strs = len(strs)

        idx = 0
        while idx < len(strs[0]) and idx < len(strs[len_strs - 1]) and strs[0][idx] == strs[len_strs - 1][idx]:
            idx += 1
        return strs[0][0:idx]


object = LongestCommonPrefix()
strs = ["flower","flow","flight"]
print(object.longestCommonPrefix(strs))
strs = ["dog","racecar","car"]
print(object.longestCommonPrefix(strs))
strs = []
print(object.longestCommonPrefix(strs))
strs = [""]
print(object.longestCommonPrefix(strs))
strs = ["", ""]
print(object.longestCommonPrefix(strs))
strs = ["c", "c"]
print(object.longestCommonPrefix(strs))
strs = ["aa", "a"]
print(object.longestCommonPrefix(strs))
strs = ["aaa", "aa", "aaa"]
print(object.longestCommonPrefix(strs))