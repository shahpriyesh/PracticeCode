class MajorityElement:
    def __init__(self):
        return

    def majorityElement(self, nums):
        maj_idx, count = 0, 1
        for idx in range(len(nums)):
            if nums[maj_idx] == nums[idx]:
                count += 1
            else:
                count -= 1

            if count == 0:
                maj_idx, count = idx, 1

        return nums[maj_idx]