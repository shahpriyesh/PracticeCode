class NegaBinary:
    def Addition(self, arr1, arr2):
        arr1_len, arr2_len = len(arr1), len(arr2)
        num1, num2 = 0, 0

        # construct first number
        for idx in range(arr1_len):
            num1 += (pow(-2, arr1_len - idx - 1) * arr1[idx])

        # construct second number
        for idx in range(arr2_len):
            num2 += (pow(-2, arr2_len - idx - 1) * arr2[idx])

        num = num1 + num2

        return num

    def DirectAddition(self, arr1, arr2):
        res = []
        carry = 0

        # keep going until any array is not empty or carry is present
        while arr1 or arr2 or carry:
            # pop the LSB or use 0
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            # possible answers are 00, 01, 10, 11 => use the LSB as answer and MSB as carry
            res.append(carry & 1)
            # negate the carry for next iteration as we are doing NegaBinary base
            carry = -(carry >> 1)

        # remove leading 0s from answer (as we are going to give answer after reverse)
        while len(res) > 1 and res[-1] == 0:
            res.pop()

        # return from MSB to LSB result
        return res[::-1]



object = NegaBinary()
arr1 = [1, 1, 1, 1, 1]
arr2 = [1, 0, 1]
print(object.DirectAddition(arr1, arr2))