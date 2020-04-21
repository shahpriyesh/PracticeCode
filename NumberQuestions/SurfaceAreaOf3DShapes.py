class SurfaceAreaOf3DShapes:
    def surfaceArea(self, grid):
        m, n = len(grid), len(grid[0])
        total_surfaces = 0

        for i in range(m):
            for j in range(n):
                cubes = grid[i][j]
                total_surfaces = total_surfaces + cubes * 6
                contact_surfaces = 2 * (cubes - 1) if cubes else 0
                total_surfaces = total_surfaces - contact_surfaces

        for i in range(m):
            for j in range(n-1):
                contact_surfaces = 2 * (min(grid[i][j], grid[i][j+1]))
                total_surfaces = total_surfaces - contact_surfaces

        for j in range(n):
            for i in range(m-1):
                contact_surfaces = 2 * (min(grid[i][j], grid[i+1][j]))
                total_surfaces = total_surfaces - contact_surfaces

        return total_surfaces


object = SurfaceAreaOf3DShapes()
grid = [[2]]
print(object.surfaceArea(grid))
grid = [
    [1,2],
    [3,4]
]
print(object.surfaceArea(grid))
grid = [
    [1,0],
    [0,2]
]
print(object.surfaceArea(grid))
grid = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
print(object.surfaceArea(grid))
grid = [
    [2,2,2],
    [2,1,2],
    [2,2,2]
]
print(object.surfaceArea(grid))