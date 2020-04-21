class IntegerToRoman:
    dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D',
            900: 'CM', 1000: 'M'}

    def __init__(self):
        pass

    def integerToRoman(self, num):
        tens = 1
        roman = ""

        while num:
            digit = (num % 10) * tens
            tens = tens * 10
            num = num // 10
            roman = self.integerSingularToRoman(digit) + roman

        return roman

    def integerSingularToRoman(self, num):
        if num in self.dict:
            return self.dict[num]

        roman = ""
        converters = [1, 5, 10, 50, 100, 500, 1000]
        idx = len(converters) - 1

        while num > 0:
            if num - converters[idx] >= 0:
                roman = roman + self.dict[converters[idx]]
                num = num - converters[idx]
            else:
                idx = idx - 1

        return roman


object = IntegerToRoman()
print(object.integerToRoman(1994))
print(object.integerToRoman(58))
print(object.integerToRoman(9))
print(object.integerToRoman(4))
print(object.integerToRoman(3))