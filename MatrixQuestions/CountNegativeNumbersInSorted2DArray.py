class CountNegativeNumbersInSorted2DArray:
    def countNegatives(self, grid):

        if len(grid) == 1:
            for i, n in enumerate(grid[0]):
                if n < 0:
                    return len(grid[0]) - i

        n = len(grid[0])
        c, r = 0, len(grid)-1
        count = 0
        while r >= 0 and c < len(grid[0]):
            if grid[r][c] < 0:
                count += n - c
                r = r - 1
            else:
                c = c + 1
        return count


object = CountNegativeNumbersInSorted2DArray()
grid = [
    [4,3,2,-1],
    [3,2,1,-1],
    [1,1,-1,-2],
    [-1,-1,-2,-3]
]
#print(object.countNegatives(grid))
grid = [
    [3,2],
    [1,0]
]
#print(object.countNegatives(grid))
grid = [
    [1,-1],
    [-1,-1]
]
#print(object.countNegatives(grid))

# Following case failed due to use of wrong 'n' in calculation
grid = [
    [5,1,0],
    [-5,-5,-5]
]
#print(object.countNegatives(grid))

# Following case failed due to not handling single row case
grid = [[7,-3]]
#print(object.countNegatives(grid))

grid = [
    [3,2],
    [-3,-3],
    [-3,-3],
    [-3,-3]
]
print(object.countNegatives(grid))