class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

# Try to understand what just happened here???
class LargestNumber:
    def largestNumber(self, nums):
        res = ''.join(sorted(map(str, nums), key=LargerNumKey))

        return res


object = LargestNumber()
print(object.largestNumber([10,2]))
print(object.largestNumber([3,30,34,5,9]))