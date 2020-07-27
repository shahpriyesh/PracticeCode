from collections import Counter

class Solution:
    def uniqueNumberOfOccurences(self, arr):
        cntr = Counter(arr)
        cntr = cntr.most_common()
        for i in range(len(cntr)-1):
            if cntr[i][1] == cntr[i+1][1]:
                return False
        return True


object = Solution()
print(object.uniqueNumberOfOccurences([1,2,2,1,1,3]))
print(object.uniqueNumberOfOccurences([1,2]))
print(object.uniqueNumberOfOccurences([-3,0,1,-3,1,1,1,-3,10,0]))