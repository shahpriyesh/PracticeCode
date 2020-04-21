'''
29. Divide Two Integers
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
[−231,  231 − 1]. For the purpose of this problem,
assume that your function returns 231 − 1 when the division result overflows.
'''

class DivideTwoIntegers:
    def divideTwoIntegers(self, dividend, divisor):
        quotient = 0

        if abs(divisor) == 1:
            return self.checkOverOrUnderFlow(dividend * divisor)

        sign = -1 if dividend < 0 else 1
        sign = sign * -1 if divisor < 0 else sign * 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            dividend = dividend - divisor
            quotient += 1

        return self.checkOverOrUnderFlow(quotient * sign)

    def checkOverOrUnderFlow(self, num):
        if num < pow(-2, 31):
            return pow(-2, 31)
        elif num > pow(2, 31) - 1:
            return pow(2, 31) - 1
        else:
            return num


object = DivideTwoIntegers()
print(object.divideTwoIntegers(10, 3))
print(object.divideTwoIntegers(7, -3))
print(object.divideTwoIntegers(1, 1))  # didn't check equals for quotient
print(object.divideTwoIntegers(-2147483648, -1))  # Time limit exceeds, overflow occured
print(object.divideTwoIntegers(2147483647, 2))  # Time limit exceeds
