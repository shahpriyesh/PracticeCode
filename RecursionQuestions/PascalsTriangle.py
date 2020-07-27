class Solution:
    def pascalsTriangle(self, numRows):
        if numRows == 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        res.append([1,1])
        if numRows == 2:
            return res

        self.pascalsTriangleUtil(res, 1, numRows)

        return res

    def pascalsTriangleUtil(self, res, curr, numRows):
        if curr+1 == numRows:
            return res

        temp = [1]
        for i in range(0, len(res[-1])-1):
            val = res[-1][i] + res[-1][i+1]
            temp.append(val)
        temp.append(1)

        res.append(temp)
        self.pascalsTriangleUtil(res, curr+1, numRows)

        return


object = Solution()
print(object.pascalsTriangle(5))