class Solution:
    def monotoneIncreasingDigits(self, N):
        Nstr = str(N)
        res = [""]
        curr = ""
        lower = 0
        upper = int(Nstr[0])

        for d in range(upper, lower-1, -1):
            curr += str(d)
            self.backtrack(Nstr, Nstr[1:], curr, res, d)
            curr = curr[:len(curr)-1]
            if res[0]:
                return res[0].lstrip('0')

        return res[0].lstrip('0')

    def backtrack(self, orig, Nstr, curr, res, lower):
        if not Nstr:
            if int(curr) <= int(orig):
                res[0] = curr
            return

        for d in range(9, lower-1, -1):
            curr += str(d)
            if int(curr) <= int(orig[:len(curr)]):
                self.backtrack(orig, Nstr[1:], curr, res, d)
            curr = curr[:len(curr)-1]
            if res[0]:
                return
        return


object = Solution()
print(object.monotoneIncreasingDigits(10))
print(object.monotoneIncreasingDigits(1234))
print(object.monotoneIncreasingDigits(332))