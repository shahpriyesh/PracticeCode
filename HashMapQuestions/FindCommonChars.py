import collections

class FindCommonChars:
    def findCommonChars(self, A):
        # create a map to hold (ch, list of appearance count)
        charMap = {}
        for word in A:
            # keep counter of characters
            cnt = [0] * 26
            for c in word:
                # index of character in counter
                chIdx = ord(c) - ord('a')
                if c in charMap:
                    # if this is newly appeared occurence than append integer entry for this appearance
                    if len(charMap[c]) != (cnt[chIdx]+1):
                        charMap[c].append(0)
                    # increase count of character based on its number of appearances
                    charMap[c][cnt[chIdx]] += 1
                else:
                    # initialize char in map with first appearance
                    charMap[c] = [1]
                # increase count of this character so that if it appears again in same word, we know it
                cnt[chIdx] += 1

        # create result list of all characters that appears as many times as words in A (which means its in all words)
        res = []
        for k, v in charMap.items():
            for x in v:
                if x == len(A):
                    res.append(k)

        return res

    def findCommonCharsUsingCounter(self, A):
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a)
        return list(res.elements())


object = FindCommonChars()
print(object.findCommonCharsUsingCounter(["bella","label","roller"]))
print(object.findCommonCharsUsingCounter(["cool","lock","cook"]))