class MaxAreaOfIsland:
    def maxAreaOfIsland(self, grid):
        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.areaSearch(grid, i, j))
        return max_area

    def areaSearch(self, grid, row, col):
        # boundary check
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return 0
        # visited check
        if grid[row][col] != 1:
            return 0

        area = 1
        # mark this cell visited
        grid[row][col] = -1

        # now do the same for all four neighbours
        area += self.areaSearch(grid, row - 1, col)
        area += self.areaSearch(grid, row + 1, col)
        area += self.areaSearch(grid, row, col - 1)
        area += self.areaSearch(grid, row, col + 1)

        return area


object = MaxAreaOfIsland()
grid = [
 [0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]
]
print(object.maxAreaOfIsland(grid))

grid = [
    [0, 0, 0, 0, 0, 0, 0, 0]
]
print(object.maxAreaOfIsland(grid))