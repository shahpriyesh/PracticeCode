class RotateImage:
    def rotateImage(self, matrix):
        pass

    def reverseImageUpDown(self, matrix):
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        return matrix

    def diagFlip(self, matrix):
        pass


object = RotateImage()
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(object.rotateImage(matrix))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(object.rotateImage(matrix))