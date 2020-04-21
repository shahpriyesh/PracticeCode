class BinarySubstring:
    def binarySubstring(self, S, N):
        for n in range(N+1):
            binRep = ""
            while(n):
                binRep = str(n & 1) + binRep
                n = n >> 1
            if S.find(binRep) == -1:
                return False
        return True


object = BinarySubstring()
print(object.binarySubstring("0110", 3))
print(object.binarySubstring("0110", 4))
print(object.binarySubstring("10010111100001110010", 10))