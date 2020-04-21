from collections import Counter

class DistantBarcodes:
    def distantBarcodes(self, barcodes):
        i = 0
        n = len(barcodes)
        res = [0]*n
        for k, v in Counter(barcodes).most_common():
            for _ in range(v):
                res[i] = k
                i += 2
                if i >= n:
                    i = 1
        return res


object = DistantBarcodes()
barcodes = [1,1,1,1,2,2,3,3]
print (object.distantBarcodes(barcodes))
