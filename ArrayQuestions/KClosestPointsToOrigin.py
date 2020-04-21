import math

class KClosestPointsToOrigin:
    def kClosest(self, points, K):
        distList = []
        for i in range(len(points)):
            distList.append((self.euclidean(points[i]), i))
        distList.sort(key=lambda x: x[0])

        res = []
        for entry in distList[:K]:
            res.append(points[entry[1]])

        return res

    def euclidean(self, point):
        x, y = 0, 1
        return math.sqrt(pow(point[x], 2) + pow(point[y], 2))


object = KClosestPointsToOrigin()
print(object.kClosest([[1,3],[-2,2]], 1))
print(object.kClosest([[3,3],[5,-1],[-2,4]], 2))