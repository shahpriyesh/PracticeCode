class FreedomTrail:
    def freedomTrail(self, ring, key):
        steps = 0
        size = len(ring) - 1
        for ch in key:
            left = ring.find(ch)
            right = size - ring.rfind(ch)
            if left < right:
                ring = self.rotate(ring, left)
            else:
                ring = self.rotate(ring, right)
            steps += (min(left, right) + 1)
        return steps

    def rotate(self, ring, k):
        size = len(ring)
        res = [0]*size
        for i in range(size):
            res[(i+k)%size] = ring[i]
        return ''.join(res)


object = FreedomTrail()
print(object.freedomTrail("godding", "gd"))
print(object.freedomTrail("godding", "godding"))
print(object.freedomTrail("abcde", "ade"))