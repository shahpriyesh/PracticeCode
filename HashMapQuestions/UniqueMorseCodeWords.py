class Solution:
    def UniqueMorseCodeWords(self, words):
        res = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            morse_word = ""
            for c in word:
                idx = ord(c) - ord('a')
                morse_word += morse[idx]
            res.add(morse_word)
        return len(res)


object = Solution()
print(object.UniqueMorseCodeWords(["gin", "zen", "gig", "msg"]))