class PowerSet:
    # This method only works if there is no duplicates in input list
    def subsets(self, nums):
        # if there are n numbers than it will have 2^n numbers in its powerset
        set_size = len(nums)
        powerset = []
        powerset_size = pow(2, set_size)

        # Go through powerset,
        # bits in each number will represent which elements should be included for that particular set
        for set_idx in range(powerset_size):
            set = []
            # number of bits to be checked is equal to number of elements that are there in set
            for i in range(set_size):
                if set_idx & (1 << i):
                    set.append(nums[i])
            powerset.append(set)
        return powerset

    # Following method will work with inputs that have duplicates
    def subsets2(self, nums):
        # if there are n numbers than it will have 2^n numbers in its powerset
        set_size = len(nums)
        powerset = []
        powerset_size = pow(2, set_size)

        nums.sort()

        # Go through powerset,
        # bits in each number will represent which elements should be included for that particular set
        for set_idx in range(powerset_size):
            set = []
            # number of bits to be checked is equal to number of elements that are there in set
            for i in range(set_size):
                if set_idx & (1 << i):
                    set.append(nums[i])
            if set not in powerset:
                powerset.append(set)
        return powerset


object = PowerSet()
nums = [4,4,4,1,4]
print(object.subsets2(nums))

'''
Value of Counter            Subset
    000                    -> Empty set
    001                    -> a
    010                    -> b
    011                    -> ab
    100                    -> c
    101                    -> ac
    110                    -> bc
    111                    -> abc
'''