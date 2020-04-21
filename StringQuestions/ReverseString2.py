class ReverseString2:
    def reverseString2(self, s, k):
        res = ""
        for i in range(0, len(s), 2 * k):
            if i + k < len(s):
                res += (s[i:i+k])[::-1]
            else:
                res += (s[i:])[::-1]

            if i + 2 * k < len(s):
                res += s[(i + k):(i + 2 * k)]
            else:
                res += s[(i + k):]
        return res


object = ReverseString2()
print(object.reverseString2("abcdefg", 2))