class MaximumSubarray:
    def maximumSubarray(self, nums):
        # Kadane's algorithm from G4G
        max_ending_here = nums[0]
        max_so_far = nums[0]

        for i in range(1, len(nums)):
            max_ending_here += nums[i]
            max_ending_here = max(max_ending_here, nums[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far


object = MaximumSubarray()
print(object.maximumSubarray([-2,1,-3,4,-1,2,1,-5,4]))

print(object.maximumSubarray([-1]))

print(object.maximumSubarray([-1, 0]))