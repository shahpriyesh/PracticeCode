class Base7:
    def base7(self, num):
        sign = 1 if num >= 0 else -1
        num = abs(num)
        res = []
        while True:
            res.append(str(num % 7))
            num //= 7
            if num == 0:
                break
        return str(sign * int(''.join(res[::-1])))


object = Base7()
print(object.base7(100))
print(object.base7(-7))
print(object.base7(0))