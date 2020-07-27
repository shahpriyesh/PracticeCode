class Solution:
    def peakIndex(self, A):
        start = 0
        end = len(A)

        while start < end:
            mid = start + ((end - start) // 2)
            if mid-1 >= 0 and mid + 1 < len(A):
                if A[mid-1] < A[mid] > A[mid+1]:
                    # we are at peak
                    return mid
                elif A[mid-1] < A[mid] < A[mid+1]:
                    # we are at rising slope
                    # peak is on our right side
                    start = mid
                else:
                    # we are at downward slope
                    # peak is on our left side
                    end = mid
            else:
                return -1
        return -1


object = Solution()
print(object.peakIndex([0,1,0]))
print(object.peakIndex([0,2,1,0]))