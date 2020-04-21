class SmallestRange2:
    def smallestRange2(self, A, K):
        avg = sum(A)/len(A)
        for i in range(len(A)):
            if A[i] > avg:
                A[i] -= K
            else:
                A[i] += K
        return max(A) - min(A)


object = SmallestRange2()
print(object.smallestRange2([1], 0))
print(object.smallestRange2([0, 10], 2))
print(object.smallestRange2([1, 3, 6], 3))

# Logic didn't work
print(object.smallestRange2([7, 8, 8], 5))