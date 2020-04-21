class DistributeCandiesToPeople:
    def distribute(self, candies, num_people):
        res = [0]*num_people
        i = 0
        while candies > 0:
            j = i % num_people
            res[j] += i+1 if i+1 < candies else candies
            candies -= i+1
            i += 1
        return res


object = DistributeCandiesToPeople()
print(object.distribute(7, 4))
print(object.distribute(10, 3))