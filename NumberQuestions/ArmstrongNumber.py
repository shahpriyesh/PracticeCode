class ArmstrongNumber:
    def armstrongNumber(self, x):
        n = len(str(x))
        return x == self._armstrong(x, n)

    def _armstrong(self, x, n):
        summ = 0
        x = str(x)
        for c in x:
            summ += pow(int(c), n)
        return summ


object = ArmstrongNumber()
print(object.armstrongNumber(153))
print(object.armstrongNumber(120))
print(object.armstrongNumber(1253))
print(object.armstrongNumber(1634))