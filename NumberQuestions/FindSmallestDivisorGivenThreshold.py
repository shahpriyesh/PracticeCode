import math

class FindSmallestDivisorGivenThreshold:
    def findSmallestDivisor(self, nums, threshold):
        numSum = sum(nums)
        divisor = numSum / threshold

        # Now find the actual divisor which would bring sum of individual number's fractions closest to threshold
        for d in range(divisor, threshold):
            numSum = 0
            for i, num in enumerate(nums):
                numSum += math.ceil(num / d)
                if numSum > threshold:
                    break

        return math.ceil(divisor)


object = FindSmallestDivisorGivenThreshold()
print(object.findSmallestDivisor([1,2,5,9], 6))
print(object.findSmallestDivisor([2,3,5,7,11], 11))
print(object.findSmallestDivisor([19], 5))