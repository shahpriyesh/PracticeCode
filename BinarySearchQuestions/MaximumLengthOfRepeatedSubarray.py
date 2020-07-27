class MaximumLengthOfRepeatedSubarray():
    def maxLenOfRepeatedSubarray_INCOMPLETE(self, A, B):
        if not A or not B:
            return 0
        if A == B:
            return len(A)

        max_len = 0

        # pre-process B for applying binary search
        C = [(i, x) for i, x in enumerate(B)]
        C.sort(key=lambda x: x[1])

        for i in range(len(A)):
            start = 0
            end = len(B)-1
            j_idx_for_search = i
            curr_instance = self.binarySearch(C, A[j_idx_for_search], start, end)

            # search until all instances of this number is searched in B
            while curr_instance != -1:

                # Linear search matched subarray
                curr_len = 0
                while i < len(A) and curr_instance < len(B) and B[curr_instance] == A[i]:
                    curr_instance += 1
                    i += 1
                    curr_len += 1

                # Update max_len
                max_len = max(max_len, curr_len)

                # Look for next instance of our target
                start = i
                curr_instance = self.binarySearch(C, A[j_idx_for_search], start, end)

        return max_len

    def binarySearch(self, arr, target, start, end):
        while start <= end:
            mid = (start + end) // 2
            if arr[mid][1] == target:
                # Is this first instance of this number?
                if mid - 1 >= 0 and arr[mid-1][1] != target:
                    return arr[mid][0]
                elif mid - 1 < 0:
                    return arr[mid][0]
                else:
                    end = mid-1
            elif arr[mid][1] > target:
                end = mid-1
            else:
                start = mid+1
        return -1


object = MaximumLengthOfRepeatedSubarray()
# print(object.maxLenOfRepeatedSubarray([1,2,3,2,1], [3,2,1,4,7]))

# print(object.maxLenOfRepeatedSubarray([0,0,0,0,1], [1,0,0,0,0]))

# print(object.maxLenOfRepeatedSubarray([1,1,0,0,1], [1,1,0,0,0]))