class Combinations:
    def combinations(self, n, k):
        res = []
        curr = []
        self.util(n, k, res, curr)
        return res

    def util(self, n, k, res, curr):
        if k == 0:
            res.append(curr[:])
            return

        for x in range(n, 0, -1):
            curr.append(x)
            self.util(x-1, k-1, res, curr)
            curr.pop()
        return


object = Combinations()
print(object.combinations(4, 2))
