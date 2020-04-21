class ThreeSum:
    def __init__(self):
        pass


    def threeSum_forZeroSum(self, nums):
        # sort numbers to bring -ve nums at front and use 2 pointers method for twosum
        nums = sorted(nums)
        resp = []

        # pick each number one by one
        for idx in range(len(nums)):
            # once we start getting positive numbers, there is no point in checking any further
            if nums[idx] > 0:
                break
            if idx > 0 and nums[idx] == nums[idx-1]:
                continue

            front = idx+1
            rear = len(nums)-1
            while front < rear:
                total = nums[idx] + nums[front] + nums[rear]
                if total == 0:
                    resp.append([nums[idx], nums[front], nums[rear]])
                    while front < rear and nums[front] == nums[front + 1]:
                        front += 1
                    while front < rear and nums[rear] == nums[rear - 1]:
                        rear -= 1
                    front += 1
                    rear -= 1
                elif total > 0:
                    rear -= 1
                else:
                    front += 1

        return resp


object = ThreeSum()
nums = [-1, 0, 1, 2, -1, -4]
print(object.threeSum_forZeroSum(nums))
nums = [-2,0,0,2,2]
print(object.threeSum_forZeroSum(nums))