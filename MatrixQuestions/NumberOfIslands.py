class NumberOfIslands:
    def numberOfIslands(self, grid):
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    islands += 1
                    self.visitIsland(grid, i, j)
        return islands

    def visitIsland(self, grid, row, col):
        # boundary check
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        # visited check
        if grid[row][col] != "1":
            return

        # mark this cell visited
        grid[row][col] = "2"

        # visit neighbouring cells
        self.visitIsland(grid, row - 1, col)
        self.visitIsland(grid, row + 1, col)
        self.visitIsland(grid, row, col - 1)
        self.visitIsland(grid, row, col + 1)

        return


object = NumberOfIslands()

grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
print(object.numberOfIslands(grid))