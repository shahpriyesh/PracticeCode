class RemoveAllAdjacentDuplicatesInString:
    def removeAllAdjacent(self, S):
        i = 0
        while i+1 < len(S):
            # check if adjacent characters are matching
            if S[i] == S[i+1]:
                # remove adjacent characters (i and i+1)
                S = S[:i] + S[i+2:] if i+2 < len(S) else S[:i]
                if i:
                    # try the previous character if it matches with the updated next one
                    i = i - 1
            else:
                # just move to next character
                i = i + 1

        return S


object = RemoveAllAdjacentDuplicatesInString()
print(object.removeAllAdjacent("abbaca"))