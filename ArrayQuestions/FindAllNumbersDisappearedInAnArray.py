class FindAllNumbersDisappearedInAnArray:
    def find(self, nums):
        for i, num in enumerate(nums):
            # if number is not at its correct location
            while nums[i]-1 != i:
                # empty its correct location
                temp = nums[num - 1]

                # if duplicate is found than break as we don't care about putting this number at right place
                if temp == num:
                    break

                # place the number at its correct location
                nums[num - 1] = num

                # now place temp at its correct location
                num = temp

        return [i+1 for i, num in enumerate(nums) if num - 1 != i]


object = FindAllNumbersDisappearedInAnArray()
print(object.find([4,3,2,7,8,2,3,1]))
print(object.find([2,1]))
print(object.find([1,1,2,4]))