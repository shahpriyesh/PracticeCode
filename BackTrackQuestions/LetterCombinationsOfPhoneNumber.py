class LetterCombinationOfPhoneNumber:
    def letterCombinations(self, digits):
        if digits == "":
            return []

        dict = {
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        curr = []
        res = []
        self.letterCombinations_Util(digits, curr, res, dict)

        return res

    def letterCombinations_Util(self, s, curr, res, charDict):
        if s == "":
            res.append(''.join(curr))
            return

        charList = charDict[s[0]]
        for char in charList:
            curr.append(char)
            self.letterCombinations_Util(s[1:], curr, res, charDict)
            curr.pop()


object = LetterCombinationOfPhoneNumber()
print(object.letterCombinations("23"))