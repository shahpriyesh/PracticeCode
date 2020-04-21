class DistanceBetweenBusStops:
    def distance(self, distance, start, destination):
        n = len(distance)
        distance.extend(distance)

        if start > destination:
            destination, start = start, destination

        sum1 = 0
        for i in range(start, destination):
            sum1 += distance[i]

        sum2 = 0
        for j in range(n + start, destination, -1):
            sum2 += distance[j-1]

        return min(sum1, sum2)


object = DistanceBetweenBusStops()
print(object.distance([1,2,3,4], 0, 1))
print(object.distance([1,2,3,4], 0, 2))
print(object.distance([1,2,3,4], 0, 3))
print(object.distance([7,10,1,12,11,14,5,0], 7, 2))