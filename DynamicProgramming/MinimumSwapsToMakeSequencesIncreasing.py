class MinSwapsToMakeSeqIncr:
    def minSwaps(self, A, B):
        swapCnt = 0
        # traverse both seq together and compare with its respecive prev value
        # if prev value is not smaller than curr than swap A[i] with B[i]
        for i in range(1, len(A)):
            if A[i-1] >= A[i] or B[i-1] >= B[i]:

                # swap ith location
                A[i], B[i] = B[i], A[i]
                # count how many swaps will be needed later on if we swap ith location
                swap1 = self.minSwaps(A[i+1:], B[i+1:])
                # backtrack
                B[i], A[i] = A[i], B[i]

                # swap (i-1)th location
                A[i-1], B[i-1] = B[i-1], A[i-1]
                # count how many swaps will be needed later on if we swap ith location
                swap2 = self.minSwaps(A[i:], B[i:])
                # backtrack
                B[i-1], A[i-1] = A[i-1], B[i-1]

                swapCnt += (1 + min(swap1, swap2))
        return swapCnt


object = MinSwapsToMakeSeqIncr()
print(object.minSwaps([1,3,5,4], [1,2,3,7]))

print(object.minSwaps([1,3,5,4,6], [1,2,3,7,8]))

print(object.minSwaps([0,4,4,5,9], [0,1,6,8,10]))

print(object.minSwaps([3,3,8,9,10], [1,7,4,6,8]))