class SingleRowKeyboard:
    def singleRowKeyboard(self, keyboard, word):
        kb = self.rearrange(keyboard)
        curr = 0
        steps = 0
        for c in word:
            steps += abs(kb[c] - curr)
            curr = kb[c]
        return steps

    def rearrange(self, keyboard):
        kb = list(keyboard)
        i = 0
        while i < len(kb):
            new_loc = ord(kb[i]) - ord('a')
            if ord(kb[i]) != ord(kb[new_loc]):
                temp = kb[new_loc]
                kb[new_loc] = i
                kb[i] = temp
            else:
                i = i + 1
        return kb


object = SingleRowKeyboard()
keyboard = "abcdefghijklmnopqrstuvwxyz"
word = "cba"
#print(object.singleRowKeyboard(keyboard, word))
keyboard = "pqrstuvwxyzabcdefghijklmno"
word = "leetcode"
print(object.singleRowKeyboard(keyboard, word))