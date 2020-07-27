class Solution:
    def findMisplacedParantheses(self, s):
        open_cnt = 0
        close_cnt = 0

        for c in s:
            if c == '(':
                open_cnt += 1
            elif c == ')':
                if open_cnt > 0:
                    open_cnt -= 1
                else:
                    close_cnt += 1

        return (open_cnt, close_cnt)


object = Solution()
print(object.findMisplacedParantheses("( ) ) ) ( ( ( )"))