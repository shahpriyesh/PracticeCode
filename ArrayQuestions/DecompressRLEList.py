class DecompressRLEList:
    def decompressRLEList(self, nums):
        res = []
        for i in range(0, len(nums), 2):
            res.extend([nums[i+1]] * nums[i])
        return res


object = DecompressRLEList()
nums = [1, 2, 3, 4]
print(object.decompressRLEList(nums))