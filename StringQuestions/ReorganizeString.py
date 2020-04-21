class ReorganizeString:
    def reorganizeString_INCORRECT(self, S):
        S = list(S)
        S.sort()
        right = len(S)-1
        left = 0
        while left < right:
            # are two adjacent characters same?
            if S[left] == S[left+1]:
                # is left side replacement candidate = (left+1)th char, same as right side replacement candidate right?
                if S[left+1] == S[right]:
                    # skip the right candidate as it can't be replaced here, move right pointer one position left
                    right -= 1
                else:
                    # yes we can swap these two chars, so that left and left+1 becomes different
                    S[left+1], S[right] = S[right], S[left+1]
                    # string is fixed up to left, now move ahead
                    left += 1
            else:
                # huh, nothing to do as chars are already different
                left += 1
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return ''
        return ''.join(S)


object = ReorganizeString()
print(object.reorganizeString("aab"))
print(object.reorganizeString("aaab"))
print(object.reorganizeString("aaaaa"))
print(object.reorganizeString("aabbbbaa"))