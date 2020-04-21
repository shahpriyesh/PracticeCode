class ReverseInteger:
    def __init__(self):
        pass

    def reverseInteger(self, x):
        resp = 0
        # register the sign
        sign = 1 if x >= 0 else -1

        # convert number into positive so that modulo operator can be used on it
        x = x * sign

        # until x becomes zero due to divisions
        while x:
            # separate out the digit
            dig = x % 10
            x = x // 10
            # construct response
            resp = (resp*10) + dig

        # check for overflow
        if resp < pow(-2, 31) or resp > pow(2, 31) - 1:
            return 0

        # return reversed digit with proper sign
        return resp * sign


object = ReverseInteger();
#print(object.reverseInteger(123))
print(object.reverseInteger(-123))
print(object.reverseInteger(120))
