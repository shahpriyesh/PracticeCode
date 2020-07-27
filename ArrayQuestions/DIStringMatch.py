class DIStringMatch:
    def diStringMatch(self, S):
        start, end = 0, len(S)
        res = []

        for c in S:
            if c == 'I':
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1

        if S[-1] == 'I':
            res.append(end)
        else:
            res.append(start)

        return res


object = DIStringMatch()
print(object.diStringMatch("IDID"))
print(object.diStringMatch("III"))
print(object.diStringMatch("DDI"))