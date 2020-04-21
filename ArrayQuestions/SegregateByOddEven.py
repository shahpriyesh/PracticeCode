class SegregateByOddEven:
    def __init__(self):
        pass

    # Takes O(n) time and O(1) space
    def segregateByOddEven(self, A):
        even = 0
        odd = len(A)-1
        while even <= odd:
            if A[even] % 2 != 0 and A[odd] % 2 == 0:
                A[even], A[odd] = A[odd], A[even]
                even += 1
                odd -= 1
            if A[even] % 2 == 0:
                even += 1
            if A[odd] % 2 != 0:
                odd -= 1
        return A

    # Takes O(n) time and O(n) space
    def segregateByOddEvenPythonically(self, A):
        return [[i for i in A if A[i] % 2 == 0] + [i for i in A if A[i] % 2 != 0]]

    # Takes O(nlgn) time and O(n) space
    def segregateByOddEvenUsingSorting(self, A):
        return sorted(A, key=lambda x: x % 2)


object = SegregateByOddEven()
A = [2, 3, 4, 5, 7, 8]
print(object.segregateByOddEven(A))