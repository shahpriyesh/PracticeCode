from collections import Counter

class Permutations:
    def permutations(self, nums):
        final = []
        self.util(nums, final, 0, len(nums))
        return final

    def util(self, nums, final, start, end):
        if start == end:
            final.append(nums[:])

        for i in range(start, end):
            nums[i], nums[start] = nums[start], nums[i]
            self.util(nums, final, start+1, end)
            nums[i], nums[start] = nums[start], nums[i]

        return

    def permutations2(self, nums):
        final = []
        self.util2(nums, final, 0, len(nums))
        return final

    def util2(self, nums, final, start, end):
        if start == end:
            if nums not in final:
                final.append(nums[:])

        for i in range(start, end):
            nums[i], nums[start] = nums[start], nums[i]
            self.util2(nums, final, start+1, end)
            nums[i], nums[start] = nums[start], nums[i]

        return

    def permutations2_way2(self, nums):
        final = []
        path = []
        self.util2_way2(Counter(nums), path, final, 0, len(nums))
        return final

    def util2_way2(self, counter, path, final, start, end):
        if start == end:
            final.append(path[:])

        for x in counter:
            if counter[x]:
                path.append(x)
                counter[x] -= 1
                self.util2_way2(counter, path, final, start + 1, end)
                counter[x] += 1
                path.pop()

        return


object = Permutations()
print(object.permutations([1, 2, 3]))

print(object.permutations2([1, 1, 2]))
print(object.permutations2_way2([1, 1, 2]))