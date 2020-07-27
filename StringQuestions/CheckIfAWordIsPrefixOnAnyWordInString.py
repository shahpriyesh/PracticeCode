class Solution:
    def checkPrefix(self, sentence, searchWord):
        sentence = sentence.split()
        for i, word in enumerate(sentence):
            if word.find(searchWord) == 0:
                return i+1
        return -1


object = Solution()
print(object.checkPrefix("i love eating burger", "burg"))
print(object.checkPrefix("this problem is an easy problem", "pro"))
print(object.checkPrefix("i am tired", "you"))
print(object.checkPrefix("i use triple pillow", "pill"))
print(object.checkPrefix("hello from the other side", "they"))