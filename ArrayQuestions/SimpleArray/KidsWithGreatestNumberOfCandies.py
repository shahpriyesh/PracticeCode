class KidsWithGreatestNumberOfCandies:
    def kidsWithCandies(self, candies, extraCandies):
        top = max(candies)
        res = []

        for candy_cnt in candies:
            if candy_cnt + extraCandies >= top:
                res.append(True)
            else:
                res.append(False)

        return res


object = KidsWithGreatestNumberOfCandies()
print(object.kidsWithCandies([2,3,5,1,3], 3))
print(object.kidsWithCandies([4,2,1,1,2], 1))
print(object.kidsWithCandies([12,1,12], 10))