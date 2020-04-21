from collections import Counter

class SetMisMatch:
    def setMismatch(self, nums):
        real = [i for i in range(1, len(nums)+1)]
        return [Counter(nums).most_common(1)[0][0], (set(real)-set(nums)).pop()]

    def setMismatch_index(self, nums):
        real = [0]*(len(nums)+1)
        ans = [0, 0]
        for i, n in enumerate(nums):
            if real[n] == n:
                ans[0] = n
            else:
                real[n] = i+1

        for i, n in enumerate(real):
            if i and i != n:
                ans[1] = i
                return ans


object = SetMisMatch()
print(object.setMismatch_index([1,2,2,4]))