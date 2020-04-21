class ReverseArrayToMaximizeArrayValue:
    def reverseToMaximize(self, nums):
        i, j = 1, len(nums)-2
        max_so_far = 0
        start, end = 0, 0

        while i < j:
            curr = abs(nums[i] - nums[i-1]) + abs(nums[j] - nums[j+1])

            # check case 1
            new = abs(nums[j] - nums[i-1]) + abs(nums[i] - nums[j+1])
            if new > curr and new > max_so_far:
                start, end = i, j
                max_so_far = new

            # check case 2
            i = i + 1
            new = abs(nums[j] - nums[i - 1]) + abs(nums[i] - nums[j + 1])
            if new > curr and new > max_so_far:
                start, end = i, j
                max_so_far = new

            # reset
            i = i - 1

            # check case 3
            j = j - 1
            new = abs(nums[j] - nums[i - 1]) + abs(nums[i] - nums[j + 1])
            if new > curr and new > max_so_far:
                start, end = i, j
                max_so_far = new

            # reset
            j = j + 1

            # Move to next indices
            i = i + 1
            j = j - 1

        nums[start:end+1] = nums[end:start-1:-1]

        summ = 0
        for i in range(0, len(nums)-1):
            summ += abs(nums[i] - nums[i + 1])

        return summ


object = ReverseArrayToMaximizeArrayValue()
print(object.reverseToMaximize([2, 3, 1, 5, 4]))
print(object.reverseToMaximize([2,4,9,24,2,1,10]))

print(object.reverseToMaximize([[2,5,1,3,4]]))