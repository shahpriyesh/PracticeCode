class NumberOfClosedIslands:
    def numberOfClosedIslands(self, grid):
        islandNum = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    if self.visitIsland(grid, i, j, islandNum):
                        islandNum += 1
        return islandNum - 2

    def visitIsland(self, grid, row, col, islandNum):
        # boundary check -> if this ever hits, that means island is spilling to boundary so its not island
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return False

        # visited check (if it is not land, it has to be water or part of same island)
        if grid[row][col] != 0:
            if grid[row][col] == 1 or grid[row][col] == islandNum:
                return True
            else:
                return False

        # mark this cell visited
        grid[row][col] = islandNum

        # visit in all four direction, if boundary hits anywhere than just return
        u = self.visitIsland(grid, row - 1, col, islandNum)
        d = self.visitIsland(grid, row + 1, col, islandNum)
        l = self.visitIsland(grid, row, col - 1, islandNum)
        r = self.visitIsland(grid, row, col + 1, islandNum)

        return u and d and l and r


object = NumberOfClosedIslands()
grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
print(object.numberOfClosedIslands(grid))
grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
print(object.numberOfClosedIslands(grid))
grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
print(object.numberOfClosedIslands(grid))

grid = [
    [0,0,1,1,0,1,0,0,1,0],
    [1,1,0,1,1,0,1,1,1,0],
    [1,0,1,1,1,0,0,1,1,0],
    [0,1,1,0,0,0,0,1,0,1],
    [0,0,0,0,0,0,1,1,1,0],
    [0,1,0,1,0,1,0,1,1,1],
    [1,0,1,0,1,1,0,0,0,1],
    [1,1,1,1,1,1,0,0,0,0],
    [1,1,1,0,0,1,0,1,0,1],
    [1,1,1,0,1,1,0,1,1,0]
]
print(object.numberOfClosedIslands(grid))
