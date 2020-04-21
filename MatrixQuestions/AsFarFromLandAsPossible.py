# https://leetcode.com/problems/as-far-from-land-as-possible/
class AsFarFromLandAsPossible:
    def __init__(self):
        pass

    def maxDistance(self, grid):
        rows = len(grid)
        columns = len(grid[0])

        x_dist = 0
        y_dist = 0

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == 1:
                    grid[i][j] = (x_dist, y_dist)
                else:
                    grid[i][j] = grid[i][j-1]

        return -1


object = AsFarFromLandAsPossible()
matrix = [
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    [1, 0, 1],
    ]
object.maxDistance(matrix)
