from collections import Counter

class ValidSudoku:
    def validSudoku(self, board):
        numRows = len(board)
        numCols = len(board[0])

        # validate rows
        for row in board:
            if not self.isValidRow(row):
                print(str(row) + " is invalid")
                return False

        # validate columns
        for col in zip(*board):
            if not self.isValidCol(col):
                print(str(col) + " is invalid")
                return False

        cubeRow = numRows // 3
        cubeCol = numCols // 3

        # construct cube and validate it
        for x in range(cubeRow * cubeCol):
            cube = [['.' for _ in range(cubeRow)] for _ in range(cubeCol)]
            for i in range(cubeRow):
                for j in range(cubeCol):
                    cube[i][j] = board[(x // 3)*cubeRow + i][(x % 3)*cubeCol + j]
            if not self.isValidCube(cube):
                print(str(cube) + " is invalid")
                return False

        return True

    def isValidRow(self, row):
        # count occurences and take most common 2, most likely 1st element will be '.' and 2nd will be most frequent num
        common = Counter(row).most_common(2)
        # if there is only 1 element and that's '.' than this row is valid, if any other number than invalid
        # if there are more than 1 element, and second element has value != 1 that means that number repeats => invalid
        return (len(common) == 1 and common.pop()[0] == '.') or common.pop()[1] == 1

    def isValidCol(self, col):
        # count occurences and take most common 2, most likely 1st element will be '.' and 2nd will be most frequent num
        common = Counter(col).most_common(2)
        # if there is only 1 element and that's '.' than this col is valid, if any other number than invalid
        # if there are more than 1 element, and second element has value != 1 that means that number repeats => invalid
        return (len(common) == 1 and common.pop()[0] == '.') or common.pop()[1] == 1

    def isValidCube(self, cube):
        # can't use 2D array directly in counter, so count row by row.
        cntr = Counter([])
        for row in cube:
            cntr.update(row)
        # count occurences and take most common 2, most likely 1st element will be '.' and 2nd will be most frequent num
        common = cntr.most_common(2)
        # if there is only 1 element and that's '.' than this cube is valid, if any other number than invalid
        # if there are more than 1 element, and second element has value != 1 that means that number repeats => invalid
        return (len(common) == 1 and common.pop()[0] == '.') or common.pop()[1] == 1


object = ValidSudoku()
board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(object.validSudoku(board))

board = [
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(object.validSudoku(board))

board = [
    [".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
print(object.validSudoku(board))

board = [
    [".",".",".",".","5",".",".","1","."],
    [".","4",".","3",".",".",".",".","."],
    [".",".",".",".",".","3",".",".","1"],
    ["8",".",".",".",".",".",".","2","."],
    [".",".","2",".","7",".",".",".","."],
    [".","1","5",".",".",".",".",".","."],
    [".",".",".",".",".","2",".",".","."],
    [".","2",".","9",".",".",".",".","."],
    [".",".","4",".",".",".",".",".","."]
]
print(object.validSudoku(board))