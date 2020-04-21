class BinarySubarraysWithSum:
    def binarySubarraysWithSum(self, A, S):
        res = 0
        # construct prefix sum
        P = [0]*(len(A)+1)
        for i in range(len(A)):
            P[i+1] = P[i] + A[i]

        left, right = 0, 1
        while len(P) > right > left:
            diff = P[right] - P[left]
            if diff < S:
                # we need bigger difference
                right += 1
            elif diff > S:
                # we need smaller difference
                left += 1
            else:
                # match found, we will go to check next subarray
                res += 1
                if right < len(P)-1:
                    right += 1
                else:
                    left += 1
        return res


object = BinarySubarraysWithSum()
print(object.binarySubarraysWithSum([1,0,1,0,1], 2))

print(object.binarySubarraysWithSum([0,0,0,0,0], 0))