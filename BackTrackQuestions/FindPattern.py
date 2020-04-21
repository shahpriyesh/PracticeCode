class FindPattern:
    def findPattern(self, haystack, needle):
        res = []
        temp = []
        self.findPatternUtil(haystack, 0, needle, res, temp)

    def findPatternUtil(self, haystack, start, needle, res, temp):
        if needle == "":
            res.append(temp)
            return

        for j, c in enumerate(needle):
            i = start
            while i < len(haystack):
                if haystack[i] == c:
                    temp.append(i)
                    self.findPatternUtil(haystack[i+1:], i+1, needle[j+1:], res, temp)
                    temp.pop()
        return