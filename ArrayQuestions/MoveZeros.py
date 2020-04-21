class MoveZeros:
    def moveZerosKeepOrder(self, nums):
        zero_idx = 0
        size = len(nums)

        # Find index of first zero
        for idx in range(size):
            if nums[idx] == 0:
                zero_idx = idx
                break

        # start from where we found first zero
        start = zero_idx
        for idx in range(start, size):
            # if value is zero just move to next index, if it is non-zero than replace with first zero available
            if nums[idx] != 0:
                # Replace zero with first non-zero value
                nums[zero_idx], nums[idx] = nums[idx], nums[zero_idx]
                # Update zero index to next
                zero_idx = zero_idx + 1

        return nums


nums = [0,1,2,0,3,2]
object = MoveZeros()
print(object.moveZerosKeepOrder(nums))