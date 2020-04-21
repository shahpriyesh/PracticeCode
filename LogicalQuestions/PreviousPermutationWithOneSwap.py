class PreviousPermutationWithOneSwap:
    def prevPermOpt1(self, A):
        n = len(A)

        # Starting from end,
        # We need to find digit that is bigger than its previous digit
        for left in reversed(range(n-1)):
            if A[left] > A[left+1]:
                break
        # if there is no digit that is bigger than last digit than there is no permutation that is smaller than current
        else:
            return A

        # starting from the bigger digit,
        # look for digit that is biggest on right side of it
        biggest = 0
        right = left
        for idx in range(left+1, n):
            # find the biggest digit that is smaller than left digit selected for swap
            if biggest < A[idx] < A[left]:
                biggest = A[idx]
                right = idx

        A[left], A[right] = A[right], A[left]
        return A

    def prevPermOpt1_LeeCode(self, A):
        n = len(A)
        for left in range(n - 2, -1, -1):
            if A[left] > A[left + 1]:
                break
        else:
            return A
        right = A.index(max(a for a in A[left + 1:] if a < A[left]), left)
        A[left], A[right] = A[right], A[left]
        return A


object = PreviousPermutationWithOneSwap()
A = [3,1,1,3]
print(object.prevPermOpt1(A))