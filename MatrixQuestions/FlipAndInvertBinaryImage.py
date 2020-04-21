class FlipAndInvertBinaryImage:
    def __init__(self):
        pass

    # works with 0s and 1s, tajes O(1) space
    def FlipAndInvertBinaryImage(self, A):
        # A is list of lists
        for row in range(len(A)):
            A[row].reverse()
            for column in range(len(A[0])):
                if A[row][column]:
                    A[row][column] = 0
                else:
                    A[row][column] = 1
        return A

    # Pythonic way, works with 0s and 1s, taken O(m*n) space
    def FlipAndInvertBinaryImagePythonically(self, A):
        return [[1 ^ num for num in row[::-1]] for row in A]
