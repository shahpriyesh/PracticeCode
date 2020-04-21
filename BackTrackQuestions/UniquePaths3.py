class UniquePaths3:
    def uniquePaths3(self, grid):
        x, y = 0, 0
        res = [0]
        total_walk = 0
        # count number of 0s to remember how many spots to cover before reaching destination
        # find out where is the location of start is?
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    x, y = i, j
                if grid[i][j] == 0:
                    total_walk += 1
        self.util(grid, x, y, 0, total_walk, res)
        return res[0]

    def util(self, grid, x, y, curr_walk, total_walk, res):
        # out of bound
        if x >= len(grid) or x < 0 or y >= len(grid[0]) or y < 0:
            return
        # already visited or obstacle
        if grid[x][y] == 3 or grid[x][y] == -1:
            return
        # destination
        if grid[x][y] == 2:
            # check if all spots were covered before reaching destination
            if curr_walk - 1 == total_walk:
                # increase result count
                res[0] += 1
            return

        # Go in all four directions
        # set visited
        temp = grid[x][y]
        grid[x][y] = 3
        curr_walk += 1
        # RIGHT
        self.util(grid, x, y + 1, curr_walk, total_walk, res)
        # LEFT
        self.util(grid, x, y - 1, curr_walk, total_walk, res)
        # UP
        self.util(grid, x - 1, y, curr_walk, total_walk, res)
        # DOWN
        self.util(grid, x + 1, y, curr_walk, total_walk, res)
        # RESET VISITED
        curr_walk -= 1
        grid[x][y] = temp

        return


object = UniquePaths3()
print(object.uniquePaths3([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
print(object.uniquePaths3([[1,0,0,0],[0,0,0,0],[0,0,0,2]]))
print(object.uniquePaths3([[0,1],[2,0]]))