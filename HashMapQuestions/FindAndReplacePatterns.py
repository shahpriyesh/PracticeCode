class FindAndReplacePatterns:
    def findAndReplace(self, words, pattern):
        final = []
        for word in words:
            if self.match(word, pattern):
                final.append(word)
        return final

    def match(self, word, pattern):
        map1 = {}
        map2 = {}
        for c, p in zip(word, pattern):
            if c not in map1:
                map1[c] = p
            if p not in map2:
                map2[p] = c
            if map1[c] != p or map2[p] != c:
                return False
        return True

object = FindAndReplacePatterns()
print(object.findAndReplace(["abc","deq","mee","aqq","dkd","ccc"], "abb"))