class MinTimeToVisitAllPoints:
    def minTimeToVisitAllPoints(self, points):
        start = points[0]
        x, y = 0, 1
        total = 0
        for idx in range(1, len(points)):
            end = points[idx]

            # see if we can move diagonally
            diag_steps = min(start[x] - end[x], start[y] - end[y])

            # see if we can move horizontally or vertically
            lateral_steps = max(abs(start[x] - end[x]), abs(start[y] - end[y])) - diag_steps
            total += (diag_steps + lateral_steps)

            start = points[idx]

        return total


object = MinTimeToVisitAllPoints();
points = [[1,1],[3,4],[-1,0]]
print(object.minTimeToVisitAllPoints(points))
points = [[3,2],[-2,2]]
print(object.minTimeToVisitAllPoints(points))