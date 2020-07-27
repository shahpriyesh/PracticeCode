class Solution:
    def CellsWithOddValuesInMatrix(self, n, m, indices):
        odds = 0
        matrix = [[0 for i in range(m)] for j in range(n)]
        for indice in indices:
            row = indice[0]
            col = indice[1]

            for j in range(m):
                matrix[row][j] += 1

            for i in range(n):
                matrix[i][col] += 1

        for i in range(n):
            for j in range(m):
                if matrix[i][j] & 1:
                    odds += 1

        return odds


object = Solution()
print(object.CellsWithOddValuesInMatrix(2, 3, [[0,1],[1,1]]))
print(object.CellsWithOddValuesInMatrix(2, 2, [[1,1],[0,0]]))