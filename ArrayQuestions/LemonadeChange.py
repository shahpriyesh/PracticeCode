class LemonadeChange:
    def lemonadeChange(self, bills):
        cnt5 = 0
        cnt10 = 0
        for bill in bills:
            if bill == 5:
                cnt5 += 1
            elif bill == 10:
                cnt10 += 1
                cnt5 -= 1
                if cnt5 < 0:
                    return False
            elif bill == 20:
                if cnt10:
                    cnt10 = cnt10 - 1
                    cnt5 = cnt5 - 1
                else:
                    cnt5 = cnt5 - 3
                if cnt5 < 0:
                    return False
        return True


object = LemonadeChange()
print(object.lemonadeChange([5,5,5,10,20]))
print(object.lemonadeChange([5,5,10]))
print(object.lemonadeChange([10,10]))
print(object.lemonadeChange([5,5,10,10,20]))