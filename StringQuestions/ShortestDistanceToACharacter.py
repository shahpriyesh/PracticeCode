class ShortestDistanceToACharacter:
    def shortestDist(self, S, C):
        forward = [0]*len(S)
        backward = [0]*len(S)
        res = [0]*len(S)
        farthest = 2*len(S)

        for i in range(len(S)):
            if S[i] != C:
                forward[i] = abs(farthest - i)
            else:
                forward[i] = 0
                farthest = i

        farthest = 2*len(S)
        for i in range(len(S)-1, -1, -1):
            if S[i] != C:
                backward[i] = abs(farthest - i)
            else:
                backward[i] = 0
                farthest = i

        i = 0
        for x, y in zip(backward, forward):
            res[i] = min(x, y)
            i += 1

        return res


object = ShortestDistanceToACharacter()
print(object.shortestDist(S = "loveleetcode", C = 'e'))