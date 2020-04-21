class ExcelSheetColumnNumber:
    def titleToNumber(self, s):
        num = 0
        base = ord('A')
        NUM_OF_CHARS = 26
        for c in s:
            num = (num * NUM_OF_CHARS) + (ord(c) - base + 1)
        return num


object = ExcelSheetColumnNumber()
print(object.titleToNumber("ZY"))