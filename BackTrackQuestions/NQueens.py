# https://leetcode.com/problems/n-queens/
class NQueens:
    def nQueens(self, n):
        board = [[0 for i in n] for j in n]

        return board

    def nQueens_Util(self, queens_placed, n, board):
        if queens_placed == n:
            return board

        for i in range(len(board)):
            for j in range(len(board[0])):
                board[i][j] = 1