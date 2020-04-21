class LuckyNumberMatrix:
    def column(self, matrix, i):
        return [row[i] for row in matrix]

    def intersection(self, lst1, lst2):
        return [value for value in lst1 if value in lst2]

    def luckyNumMat(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        rowMat = [0]*m
        colMat = [0]*n

        for i in range(m):
            rowMat[i] = min(matrix[i])

        for j in range(n):
            colMat[j] = max(self.column(matrix, j))

        return self.intersection(rowMat, colMat)


object = LuckyNumberMatrix()
matrix = [[3,7,8],[9,11,13],[15,16,17]]
print(object.luckyNumMat(matrix))
matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(object.luckyNumMat(matrix))
matrix = [[7,8],[1,2]]
print(object.luckyNumMat(matrix))