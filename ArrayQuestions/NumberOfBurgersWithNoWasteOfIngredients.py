class Solution:
    def numOfBurgers_INCORRECT(self, tomatoSlices, cheeseSlices):
        burger = cheeseSlices
        if tomatoSlices < 2 * cheeseSlices:
            return []
        if tomatoSlices % 2 != 0:
            return []

        jumbo = tomatoSlices // 4
        tomatoSlices = tomatoSlices % 4
        if jumbo == 0:
            small = tomatoSlices // 2
        else:
            small = 0

        while jumbo > 0 and jumbo + small < burger:
            jumbo -= 1
            small += 2

        if tomatoSlices == 2:
            jumbo += 1
            small -= 1

        if jumbo + small > burger:
            return []
        else:
            return [jumbo, small]

    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        if tomatoSlices < 2 * cheeseSlices:
            return []
        if tomatoSlices % 2 != 0:
            return []

        small = (2*cheeseSlices) - (tomatoSlices // 2)
        jumbo = (tomatoSlices // 2) - cheeseSlices

        if small < 0 or jumbo < 0:
            return []
        else:
            return [jumbo, small]


object = Solution()
print(object.numOfBurgers(16, 7))
print(object.numOfBurgers(17, 4))
print(object.numOfBurgers(4, 17))
print(object.numOfBurgers(0, 0))

# This failed due to case where we were counting only jumbo, and jumbo>0 not allowing to count small
print(object.numOfBurgers(2, 1))

# This failed due to patchy logic
print(object.numOfBurgers(3962, 1205))

# After changing way to solve the issue, this failed due to big numbers
print(object.numOfBurgers(2385088, 164763))