class DecryptStringFromAlphabetToIntegerMapping:
    def decryptStringFromAlphabetToIntegerMapping(self, s):
        idx = 0
        res = ""
        while idx < len(s):
            if idx + 2 < len(s) and s[idx+2] == "#":
                res += chr(ord('a') + int(s[idx:idx+2]) - 1)
                idx += 3
            else:
                res += chr(ord('a') + int(s[idx]) - 1)
                idx += 1
        return res


object = DecryptStringFromAlphabetToIntegerMapping()
print(object.decryptStringFromAlphabetToIntegerMapping("10#11#12"))
print(object.decryptStringFromAlphabetToIntegerMapping("1326#"))
print(object.decryptStringFromAlphabetToIntegerMapping("25#"))
print(object.decryptStringFromAlphabetToIntegerMapping("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"))