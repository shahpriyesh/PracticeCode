class PrintWordsVertically:
    def printWordsVertically(self, s):
        words = s.split()
        columns = max(map(len, words))
        res = [""] * columns

        for i in range(len(words)):
            words[i] += " "*(columns - len(words[i]))

        for word in words:
            for j in range(columns):
                res[j] += word[j]

        return list(map(str.rstrip, res))


object = PrintWordsVertically()
print(object.printWordsVertically("HOW ARE YOU"))
print(object.printWordsVertically("TO BE OR NOT TO BE"))
print(object.printWordsVertically("CONTEST IS COMING"))