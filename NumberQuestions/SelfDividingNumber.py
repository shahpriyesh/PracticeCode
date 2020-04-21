class SelfDividingNumber:
    def selfDevidingNumber(self, left, right):
        result = []
        for num in range(left, right+1):
            for digit in str(num):
                if digit == '0':
                    break
                if num % int(digit) != 0:
                    break
            else:
                result.append(num)
        return result


object = SelfDividingNumber()
print(object.selfDevidingNumber(10, 20))