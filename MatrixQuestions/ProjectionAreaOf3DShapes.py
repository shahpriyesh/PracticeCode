class ProjectionAreaOf3DShapes:
    def projection(self, grid):
        m = len(grid)
        n = len(grid[0])

        cnt = 0
        # look from top view, any shape that is zero => represents empty space
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    cnt += 1

        # look from left-right side view, max in row => represents shape size
        for i in range(m):
            cnt += max(grid[i])

        # look from top-bottom view, max in column => represents shape size
        def column(grid, i):
            return [row[i] for row in grid]
        for j in range(n):
            cnt += max(column(grid, j))

        return cnt


object = ProjectionAreaOf3DShapes()
print(object.projection([[2]]))
print(object.projection([[1,2],[3,4]]))
print(object.projection([[1,0],[0,2]]))
print(object.projection([[1,1,1],[1,0,1],[1,1,1]]))
print(object.projection([[2,2,2],[2,1,2],[2,2,2]]))