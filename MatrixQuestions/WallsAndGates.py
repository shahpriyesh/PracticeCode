INF = 2147483647

class WallsAndGates:
    def wallsAndGates(self, grid):
        visited = [[(False, 0, 0) for i in range(len(grid))] for i in range(len(grid[0]))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    self.traverseRoom(grid, i, j, i, j, 0, visited)
        return grid

    def traverseRoom(self, grid, gateRow, gateCol, row, col, dist, visited):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
            return

        # look for obstacle
        if grid[row][col] == -1:
            return

        # look for another gate
        if (row != gateRow or col != gateCol) and grid[row][col] == 0:
            return

        # look if this place was visited
        if visited[row][col][0] and visited[row][col][1] == gateRow and visited[row][col][2] == gateCol:
            return

        # visit this part of room and mark to nearest door
        grid[row][col] = min(dist, grid[row][col])

        visited[row][col] = (True, gateRow, gateCol)

        # traverse in all directions
        self.traverseRoom(grid, gateRow, gateCol, row - 1, col, dist + 1, visited)
        self.traverseRoom(grid, gateRow, gateCol, row + 1, col, dist + 1, visited)
        self.traverseRoom(grid, gateRow, gateCol, row, col - 1, dist + 1, visited)
        self.traverseRoom(grid, gateRow, gateCol, row, col + 1, dist + 1, visited)

        return


object = WallsAndGates()
grid = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
print(object.wallsAndGates(grid))
grid = [[0,-1],[2147483647,2147483647]]
print(object.wallsAndGates(grid))