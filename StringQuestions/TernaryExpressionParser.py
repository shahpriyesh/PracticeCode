class TernaryExpressionParser():
    def ternaryExpressionParser(self, s):
        res = ""
        i = len(s)-1

        while i >= 0:
            if s[i] == '?':
                if s[i-1] == 'T':
                    res = s[i+1]
                    s = s[0:i-1] + s[i+1] + s[i+3:]
                else:
                    res = s[i + 3]
                    s = s[0:i-1] + s[i+3:]
            i -= 1

        return res


object = TernaryExpressionParser()
print(object.ternaryExpressionParser("F?1:T?3:1"))
print(object.ternaryExpressionParser("T?2:3"))
print(object.ternaryExpressionParser("T?T?F:5:3"))