class RomanToInteger:
    def romanToInteger(self, s):
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i = 0
        num = 0
        while i + 1 < len(s):
            if romanDict[s[i + 1]] > romanDict[s[i]]:
                num += (romanDict[s[i + 1]] - romanDict[s[i]])
                i += 2
            else:
                num += romanDict[s[i]]
                i += 1
        if i != len(s):
            num += romanDict[s[i]]
        return num


object = RomanToInteger()
print(object.romanToInteger("III"))
print(object.romanToInteger("IV"))
print(object.romanToInteger("IX"))
print(object.romanToInteger("LVIII"))
print(object.romanToInteger("MCMXCIV"))