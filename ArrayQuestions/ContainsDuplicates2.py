class ContainsDuplicates2:
    def containsDuplicates2(self, nums, k):
        hmap = {}
        for i, num in enumerate(nums):
            if num not in hmap:
                hmap[num] = [i]
            else:
                # check if out target matches
                if i - hmap[num][-1] <= k:
                    return True
                hmap[num].append(i)
        return False


object = ContainsDuplicates2()
print(object.containsDuplicates2([1,2,3,1], 3))
print(object.containsDuplicates2([1,0,1,1], 1))
print(object.containsDuplicates2([1,2,3,1,2,3], 2))