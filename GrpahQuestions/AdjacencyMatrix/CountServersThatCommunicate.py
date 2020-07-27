class CountServersThatCommunicate:
    def countServers(self, grid):
        # rowStore contains servers seen in ith row
        rowStore = [0 for i in range(len(grid))]
        # colStore contains servers seen in jth col
        colStore = [0 for j in range(len(grid[0]))]

        count = 0

        # traverse the grid and populate rowStore and colStore
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    rowStore[i] += 1
                    colStore[j] += 1

        # traverse the grid and for each server check either rowStore or colStore is +ve value>1 (not server itself)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and (rowStore[i] > 1 or colStore[j] > 1):
                    count += 1

        return count


object = CountServersThatCommunicate()
print(object.countServers([[1,0],[0,1]]))
print(object.countServers([[1,0],[1,1]]))
print(object.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]))