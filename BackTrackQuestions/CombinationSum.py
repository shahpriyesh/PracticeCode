class CombinationSum:
    def combinationSum3(self, k, n):
        final = []
        res = []
        self.combinationSum3_Util(k, n, 0, res, final)
        return final

    def combinationSum3_Util(self, k, n, used, res, final):
        if used == k:
            if sum(res) == n:
                final.append(list(res))
            return

        j = 1 if not res else res[-1] + 1
        for i in range(j, 10):
            res.append(i)
            self.combinationSum3_Util(k, n, used + 1, res, final)
            res.pop()
        return


object = CombinationSum()
print(object.combinationSum3(3, 7))