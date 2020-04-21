import collections

class IncreasingDecreasingString:
    def incDecString(self, s):
        counter = collections.Counter(s)
        res = ''
        while counter:
            for c in sorted(counter):
                res += c
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]

            for c in sorted(counter, reverse=True):
                res += c
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]

        return res


object = IncreasingDecreasingString()
print(object.incDecString("aaaabbbbcccc"))
print(object.incDecString("rat"))
print(object.incDecString("leetcode"))
print(object.incDecString("ggggggg"))
print(object.incDecString("spo"))