class PerformStringShifts:
    def performStringShifts(self, s, shifts):
        total = 0
        for shift in shifts:
            if shift[0] == 0:
                total -= shift[1]
            else:
                total += shift[1]

        if total < 0:
            total = len(s) + total

        return self.rotateLeftByK(s, total)

    def rotateLeftByK(self, s, k):
        s = list(s)

        s[:k] = reversed(s[:k])
        s[k:] = reversed(s[k:])
        s = reversed(s)
        return ''.join(s)

    def rotateRightByK(self, s, k):
        s = list(s)

        s[len(s)-k:] = reversed(s[len(s)-k:])
        s[:len(s)-k] = reversed(s[:len(s)-k])
        s = reversed(s)
        return ''.join(s)


object = PerformStringShifts()
print(object.performStringShifts("abc", [[0, 1], [1, 2]]))
print(object.performStringShifts("abcd", [[0, 1], [1, 2], [0, 4]]))
print(object.rotateLeftByK("abcd", 1))
print(object.rotateRightByK("abcd", 1))