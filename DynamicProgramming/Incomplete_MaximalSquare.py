class MaximalSquare:
    def maximalSquare(self, matrix):
        mc = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                count = 0
                if matrix[i][j] == 1:
                    matrix[i][j] = 'x'
                    self.checkIfSquare(matrix, i, j, count)
                    if count:
                        mc = max(mc, count + 1)
        return mc

    def checkIfSquare(self, matrix, i, j, count):
        if i >= len(matrix) or j >= len(matrix[0]):
            return

        if matrix[i][j+1] != 1 or matrix[i+1][j] != 1 or matrix[i+1][j+1] != 1:
            return

        matrix[i][j + 1] = 'x'
        matrix[i + 1][j] = 'x'
        matrix[i + 1][j + 1] = 'x'

        count = count + 3

        self.checkIfSquare(matrix, i, j+1, count)
        self.checkIfSquare(matrix, i + 1, j, count)
        self.checkIfSquare(matrix, i + 1, j + 1, count)

        return


object = MaximalSquare()
matrix = [
[1, 0, 1, 0, 0],
[1, 0, 1, 1, 1],
[1, 1, 1, 1, 1],
[1, 0, 0, 1, 0]
]
print(object.maximalSquare(matrix))