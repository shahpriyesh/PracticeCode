class WildcardMatching:
    # FOLLOWING IS COPIED SOLUTION TO UNDERSTAND HOW IT WORKS
    def wildcardMatching(self, s, p):
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur = p_cur + 1
            elif star != -1:
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False

        while p_cur < len(p) and p[p_cur] == '*':
            p_cur = p_cur + 1

        if p_cur == len(p):
            return True

        return False


object = WildcardMatching()
print(object.wildcardMatching("aa", "a"))
print(object.wildcardMatching("aa", "*"))
print(object.wildcardMatching("cb", "?a"))
print(object.wildcardMatching("adceb", "*a*b"))
print(object.wildcardMatching("acdcb", "a*c?b"))