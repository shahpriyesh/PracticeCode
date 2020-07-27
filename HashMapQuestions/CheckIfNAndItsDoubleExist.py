class CheckIfNAndItsDoubleExist:
    def check(self, arr):
        hmap = {}
        cnt = 0

        for num in arr:
            if num:
                hmap[num] = 2*num
            else:
                # special handling for 0
                cnt += 1
                hmap[num] = cnt

        for num in arr:
            if num:
                if 2*num in hmap:
                    return True
            else:
                # special handling for 0
                if hmap[num] > 1:
                    return True

        return False


object = CheckIfNAndItsDoubleExist()
print(object.check([10,2,5,3]))
print(object.check([7,1,14,11]))
print(object.check([3,1,7,11]))

# Failed because 0's double is 0 and its in map :(
print(object.check([-2,0,10,-19,4,6,-8]))

# Failed because 0's double is 0 and there are two zeroes
print(object.check([0, 0]))