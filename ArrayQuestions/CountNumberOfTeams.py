class Solution:
    def countNumberOfTeams(self, rating):
        res = 0
        for i in range(len(rating)-2):
            for j in range(i+1, len(rating)-1):
                for k in range(j+1, len(rating)):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        res += 1
        return res


object = Solution()
print(object.countNumberOfTeams([2,5,3,4,1]))
print(object.countNumberOfTeams([2,1,3]))
print(object.countNumberOfTeams([1,2,3,4]))