class Solution:
    def KWeakestRows(self, mat, k):
        weak = [0]*len(mat)

        for i in range(len(mat)):
            soldiers = self.countSoldiers(mat[i])
            weak[i] = (soldiers, i)

        weak.sort(key=lambda x:(x[0], x[1]))
        weak = [x[1] for x in weak]
        return weak[:k]

    def countSoldiers(self, row):
        start = 0
        end = len(row)-1

        while start <= end:
            mid = (start + end) // 2
            if mid + 1 < len(row):
                if row[mid] > row[mid + 1]:
                    # mid is soldier and mid+1 is civilian
                    return mid + 1  # number of soldiers in this row (count from 1)
                elif row[mid] == 1:
                    # mid and mid+1 both are soldiers
                    start = mid + 1
                else:
                    # mid is civilian
                    end = mid - 1
            else:
                return mid + 1
        return 0


object = Solution()
mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
print(object.KWeakestRows(mat, k))

mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
print(object.KWeakestRows(mat, k))

mat = [[1,0],[0,0],[1,0]]
k = 2
print(object.KWeakestRows(mat, k))