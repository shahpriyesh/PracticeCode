class Solution:
    def MinIncToMakeArrUnique_TLE(self, A):
        hmap = set()
        steps = 0
        for i in range(len(A)):
            while A[i] in hmap:
                steps += 1
                A[i] += 1
            hmap.add(A[i])
        return steps


object = Solution()
print(object.MinIncToMakeArrUnique([1,2,2]))
print(object.MinIncToMakeArrUnique([3,2,1,2,1,7]))