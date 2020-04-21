class CountOfSmallerNumbersAfterSelf:
    def countSmaller(self, nums):
        res = []
        for i in range(len(nums)):
            count = 0
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            res.append(count)
        return res

    def countSmallerMergeSort(self, nums):
        print(nums)
        smaller = [0]*len(nums)
        self.mergeSort(list(enumerate(nums)), smaller)
        return smaller

    def mergeSort(self, nums, smaller):
        if not nums:
            return []
        if len(nums) == 1:
            return nums
        half = len(nums) // 2

        left = self.mergeSort(nums[:half], smaller)
        right = self.mergeSort(nums[half:], smaller)

        merged = []
        i, j = 0, 0
        while i<len(left) and j<len(right):
            if left[i][1] < right[j][1]:
                merged.append(left[i])
                i += 1
            else:
                # because right element is smaller than current left element
                # this is opportunity for us to count this element as smaller than current left element
                bigger_elem_idx = left[i][0]
                smaller[bigger_elem_idx] += 1

                merged.append(right[j])
                j += 1

        while i<len(left):
            merged.append(left[i])
            i += 1

        while j < len(right):
            merged.append(right[j])
            j += 1

        return merged


object = CountOfSmallerNumbersAfterSelf()
print(object.countSmallerMergeSort([]))
print(object.countSmallerMergeSort([5,2,6,1]))
print(object.countSmallerMergeSort([5,3,7,5,4,3,7,9,8,2,2,6,1]))