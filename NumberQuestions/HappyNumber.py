class Solution:
    def happyNumber(self, n):
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = str(n)
            temp = 0
            for c in n:
                temp += pow(int(c), 2)
            n = temp
        return True


object = Solution()
print(object.happyNumber(19))
print(object.happyNumber(2))