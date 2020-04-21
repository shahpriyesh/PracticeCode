class FindAnagramMappings:
    def anagramMappingWithDuplicates(self, A, B):
        amap = {}
        for i, n in enumerate(B):
            if n in amap:
                amap[n].append(i)
            else:
                amap[n] = [i]

        res = []
        for n in A:
            res.append(amap[n].pop())

        return res

    def anagramMapping(self, A, B):
        amap = {val: idx for idx, val in enumerate(B)}
        return [amap[val] for val in A]


object = FindAnagramMappings()
print(object.anagramMapping([12, 28, 46, 32, 50], [50, 12, 32, 46, 28]))
print(object.anagramMappingWithDuplicates([12, 28, 46, 32, 50, 12], [50, 12, 32, 46, 12, 28]))