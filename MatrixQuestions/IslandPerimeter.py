class IslandPerimeter:
    def islandPerimeter(self, grid):
        numRow = len(grid)
        numCol = len(grid[0])
        found = False
        for i in range(numRow):
            for j in range(numCol):
                if grid[i][j]:
                    found = True
                    break
            if found:
                break

        res = [0]
        self.perimeterCheck(grid, i, j, res)
        return res[0]

    def perimeterCheck(self, grid, row, column, res):
        if row < 0 or row >= len(grid) or column < 0 or column >= len(grid[0]):
            return
        if grid[row][column] != 1:
            return

        # count sides that are not covered by neighbouring land cell
        res[0] += (4 - self.neighbourCount(grid, row, column))

        # mark this cell visited
        grid[row][column] = -1

        # now do the same for all four neighbours
        self.perimeterCheck(grid, row - 1, column, res)
        self.perimeterCheck(grid, row + 1, column, res)
        self.perimeterCheck(grid, row, column - 1, res)
        self.perimeterCheck(grid, row, column + 1, res)

        return

    def neighbourCount(self, grid, row, col):
        cnt = 0
        # UP
        if (row - 1) >= 0 and grid[row - 1][col]:
            cnt += 1
        # DOWN
        if (row + 1) < len(grid) and grid[row + 1][col]:
            cnt += 1
        # LEFT
        if (col - 1) >= 0 and grid[row][col - 1]:
            cnt += 1
        # RIGHT
        if (col + 1) < len(grid[0]) and grid[row][col + 1]:
            cnt += 1
        return cnt


object = IslandPerimeter()
grid = [
    [0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [1,1,0,0]
]
print(object.islandPerimeter(grid))

grid = [
    [1],
    [0]
]
print(object.islandPerimeter(grid))