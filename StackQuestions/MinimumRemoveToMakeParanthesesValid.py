class MinimumRemoveToMakeValidParantheses:
    def minRemove(self, s):
        # go left to right
        res = ""
        open_cnt = close_cnt = 0
        curr = 0
        while curr < len(s):
            if s[curr] == '(':
                open_cnt += 1
            if s[curr] == ')':
                close_cnt += 1
            if close_cnt > open_cnt:
                close_cnt = 0
                open_cnt = 0
            elif curr < len(s):
                res += s[curr]
            curr += 1

        s = res

        # go right to left
        res = ""
        open_cnt = close_cnt = 0
        curr = len(s)-1
        while curr >= 0:
            if s[curr] == '(':
                open_cnt += 1
            if s[curr] == ')':
                close_cnt += 1
            if open_cnt > close_cnt:
                close_cnt = 0
                open_cnt = 0
            elif curr < len(s):
                res = s[curr] + res
            curr -= 1

        return res


object = MinimumRemoveToMakeValidParantheses()
print(object.minRemove("lee(t(c)o)de)"))
print(object.minRemove("a)b(c)d"))
print(object.minRemove("))(("))
print(object.minRemove("(a(b(c)d)"))

print(object.minRemove("a)b(c)d"))