class Solution:
    def queriesOnAPermutationWithKey(self, queries, m):
        arr = [i for i in range(1, m+1)]
        res = []
        for query in queries:
            for i in range(m):
                if arr[i] == query:
                    arr.pop(i)
                    res.append(i)
                    break
            arr.insert(0, query)
        return res


object = Solution()
print(object.queriesOnAPermutationWithKey([3,1,2,1], 5))
print(object.queriesOnAPermutationWithKey([4,1,2,2], 4))
print(object.queriesOnAPermutationWithKey([7,5,5,8,3], 8))