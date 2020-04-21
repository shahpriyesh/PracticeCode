class VerifyingAnAlienDictionary:
    def verify(self, words, order):
        pass


object = VerifyingAnAlienDictionary()
print(object.verify(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(object.verify(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(object.verify(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))