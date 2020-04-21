class MinFlips:
    def minFlips(self, a, b, c):
        print("a = " + format(a, '08b'))
        print("b = " + format(b, '08b'))
        print("c = " + format(c, '08b'))
        flips = 0
        for i in range(32):
            mask = 1 << i
            abit, bbit, cbit = a & mask, b & mask, c & mask
            if abit | bbit != cbit:
                if abit & bbit:
                    flips += 2
                else:
                    flips += 1
        return flips


object = MinFlips()
print(object.minFlips(2, 6, 5))
print(object.minFlips(4, 2, 7))
print(object.minFlips(1, 2, 3))