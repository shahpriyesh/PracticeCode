class Solution:
    def deleteColumnsToMakeSorted(self, A):
        deletion = 0
        # for each column
        for c in range(len(A[0])):
            temp = A[0][c]
            # for each word
            for w in range(1, len(A)):
                if A[w][c] < temp:
                    deletion += 1
                    break
                else:
                    temp = A[w][c]
        return deletion


object = Solution()
print(object.deleteColumnsToMakeSorted(["cba","daf","ghi"]))
print(object.deleteColumnsToMakeSorted(["a", "b"]))
print(object.deleteColumnsToMakeSorted(["zyx","wvu","tsr"]))