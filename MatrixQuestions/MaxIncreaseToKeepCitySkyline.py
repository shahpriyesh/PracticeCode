class MaxIncreaseToKeepCitySkyline:
    def skyline(self, grid):
        m = len(grid)
        n = len(grid[0])
        maxRow = [0]*m
        maxCol = [0]*n
        final_sum = 0

        for i in range(m):
            maxRow[i] = max(grid[i])

        for j in range(n):
            maxCol[j] = max(self.column(grid, j))

        for i in range(m):
            for j in range(n):
                final_sum += min(maxRow[i], maxCol[j]) - grid[i][j]

        return final_sum

    def column(self, grid, i):
        return [row[i] for row in grid]


object = MaxIncreaseToKeepCitySkyline()
grid = [
    [3, 0, 8, 4],
    [2, 4, 5, 7],
    [9, 2, 6, 3],
    [0, 3, 1, 0]
]
print(object.skyline(grid))

