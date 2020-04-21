'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.
'''

class MaximumSubarray:
    def maximumSubarray(self, nums):
        if not nums:
            return 0

        front_add = [0 for i in range(len(nums))]
        front_add[0] = nums[0]
        max_front_sum_idx = 0
        max_front_sum = front_add[0]

        for i in range(1, len(nums)):
            front_add[i] = front_add[i-1] + nums[i]
            if max_front_sum < front_add[i]:
                max_front_sum = front_add[i]
                max_front_sum_idx = i

        rear_add = [0 for i in range(max_front_sum_idx + 1)]
        rear_add[max_front_sum_idx] = nums[max_front_sum_idx]
        max_rear_sum_idx = max_front_sum_idx
        max_rear_sum = rear_add[max_front_sum_idx]

        for i in range(max_front_sum_idx - 1, -1, -1):
            rear_add[i] = rear_add[i+1] + nums[i]
            if max_rear_sum < rear_add[i]:
                max_rear_sum = rear_add[i]
                max_rear_sum_idx = i

        return max_rear_sum


object = MaximumSubarray()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(object.maximumSubarray(nums))