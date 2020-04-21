class GlobalAndLocalInversions:
    def globalAndLocalInversions(self, A):
        # all local inversions are already global inversions
        # thus all we need to find is that is there any additional global inversions that exist?
        # to find it, we need to see if ith num is lesser than any number coming at or after (i+2)th
        # this is O(n^2),
        # but actually we only need to check with min(A[i+2],....,A[n]) so we can keep running min starting from end.
        B = [0]*len(A)
        minn = float('inf')
        for i in range(len(A)-1, -1, -1):
            minn = min(minn, A[i])
            B[i] = minn

        for i in range(len(A)-2):
            if A[i] > B[i+2]:
                return False

        return True


object = GlobalAndLocalInversions()
print(object.globalAndLocalInversions([1,0,2]))
print(object.globalAndLocalInversions([1,2,0]))
print(object.globalAndLocalInversions([1,0,2,5,4,6,7,8,3]))