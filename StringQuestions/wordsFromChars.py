class WordsFromChars:
    def __init__(self):
        pass

    def countCharsOfFormedWordsFromChars(self, words, chars):
        charmap = {}
        result = 0

        for c in chars:
            if c in charmap:
                charmap[c] += 1
            else:
                charmap[c] = 1

        for word in words:

            flag = True
            dummy_charmap = charmap.copy()
            wordlen = len(word)

            for idx in range(wordlen):
                if word[idx] not in dummy_charmap or dummy_charmap[word[idx]] == 0:
                    flag = False
                    break
                dummy_charmap[word[idx]] -= 1

            if flag:
                result += wordlen

        return result


object = WordsFromChars()
words = ["cat","bt","hat","tree"]
chars = "atach"
print(object.countCharsOfFormedWordsFromChars(words, chars))