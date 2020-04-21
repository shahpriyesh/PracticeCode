class CustomSortString:
    def customSortString(self, S, T):
        customSorted = {}
        customSorting = [0] * 26
        res = ""

        for i, c in enumerate(S):
            customSorted[c] = i

        for c in T:
            if c in customSorted:
                customSorting[customSorted[c]] += 1
            else:
                res += c

        for k,v in customSorted.items():
            res += (k * customSorting[v])

        return res


object = CustomSortString()
print(object.customSortString("cba", "abcd"))