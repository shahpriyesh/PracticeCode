class IndexPairsOfAString:
    def indexPairs(self, text, words):
        res = []
        for word in words:
            startList = [i for i in range(len(text)) if text.startswith(word, i)]
            for start in startList:
                res.append([start, start + len(word) - 1])
        return res


object = IndexPairsOfAString()
print(object.indexPairs("thestoryofleetcodeandme", ["story","fleet","leetcode"]))
print(object.indexPairs("ababa", ["aba","ab"]))