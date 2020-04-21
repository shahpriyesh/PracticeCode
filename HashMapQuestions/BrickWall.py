class BrickWall:
    def brickWall(self, wall):
        wallMap = {}
        for row in wall:
            summ = 0
            for i in range(len(row)-1):
                summ += row[i]
                if summ in wallMap:
                    wallMap[summ] += 1
                else:
                    wallMap[summ] = 1

        return len(wall) - (max(wallMap.values()) if len(wallMap.values()) else 0)


object = BrickWall()
wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
print(object.brickWall(wall))

wall = [[1],[1],[1]]
print(object.brickWall(wall))