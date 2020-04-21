# https://leetcode.com/problems/regions-cut-by-slashes/

class RegionsCutBySlashes:
    def __init__(self):
        pass

    def dfs_check(self, upscale, i, j, M, N):
        if i >= 0 and j >= 0 and i < M and j < N and upscale[i][j] == 0:
            upscale[i][j] = 1
            self.dfs_check(upscale, i - 1, j, M, N)
            self.dfs_check(upscale, i + 1, j, M, N)
            self.dfs_check(upscale, i, j - 1, M, N)
            self.dfs_check(upscale, i, j + 1, M, N)

    # https://leetcode.com/problems/regions-cut-by-slashes/discuss/205674/C%2B%2B-with-picture-DFS-on-upscaled-grid
    def regionsCutBySlashes_byDFSonUpscaledGrid(self, grid):
        M = len(grid)
        N = len(grid[0])
        upscale = [[0 for i in range(M*3)] for j in range(N*3)]
        regions = 0

        for i in range(M):
            for j in range(N):
                if grid[i][j] == "/":
                    upscale[i * 3][j * 3 + 2] = upscale[i * 3 + 1][j * 3 + 1] = upscale[i * 3 + 2][j * 3] = 1
                elif grid[i][j] == "\\":
                    upscale[i * 3][j * 3] = upscale[i * 3 + 1][j * 3 + 1] = upscale[i * 3 + 2][j * 3 + 2] = 1

        for i in range(M*3):
            for j in range(N*3):
                if upscale[i][j] == 0:
                    self.dfs_check(upscale, i, j, M*3, N*3)
                    regions += 1

        return regions

    # https://leetcode.com/problems/regions-cut-by-slashes/discuss/205680/JavaC%2B%2BPython-Split-4-parts-and-Union-Find
    def regionsBySlashes_ByUnionFind(self, grid):
        f = {}
        def find(x):
            f.setdefault(x, x)
            if x != f[x]:
                f[x] = find(f[x])
            return f[x]
        def union(x, y):
            f[find(x)] = find(y)

        for i in range(len(grid)):
            for j in range(len(grid)):
                if i:
                    union((i - 1, j, 2), (i, j, 0))
                if j:
                    union((i, j - 1, 1), (i, j, 3))
                if grid[i][j] != "/":
                    union((i, j, 0), (i, j, 1))
                    union((i, j, 2), (i, j, 3))
                if grid[i][j] != "\\":
                    union((i, j, 3), (i, j, 0))
                    union((i, j, 1), (i, j, 2))
        return len(set(map(find, f)))


object = RegionsCutBySlashes()
grid = ["/\\","\\/"]
print(object.regionsCutBySlashes_byDFSonUpscaledGrid(grid))
