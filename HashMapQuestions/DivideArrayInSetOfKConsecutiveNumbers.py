class DivideArrayInSetOfKConsecutiveNumbers:
    def divideArray(self, nums, k):
        # first check if array contains enough elements to be multiple of k
        if len(nums) % k != 0:
            return False

        # Now lets reduce number and try to fit it between 0 to k-1
        numMap = {x: 0 for x in range(k)}
        for num in nums:
            numMap[num % k] += 1

        # see if all values in map for each key is not same
        return (len(set(numMap.values())) == 1)


object = DivideArrayInSetOfKConsecutiveNumbers()
nums = [1,2,3,3,4,4,5,6]
k = 4
print(object.divideArray(nums, k))
nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
print(object.divideArray(nums, k))
nums = [3,3,2,2,1,1]
k = 3
print(object.divideArray(nums, k))
nums = [1,2,3,4]
k = 3
print(object.divideArray(nums, k))