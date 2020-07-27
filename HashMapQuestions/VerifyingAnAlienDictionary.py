class Solution:
    # Following logic does not work because you only need to check second character when first char is same.
    def VerifyingAnAlienDictionary_INCORRECT(self, words, order):
        hmap = {x: i for i, x in enumerate(order)}

        longest = 0
        for word in words:
            longest = max(longest, len(word))

        idx = 0
        while idx < longest:
            prev_pos = 0
            for word in words:
                if idx < len(word):
                    if hmap[word[idx]] < prev_pos:
                        return False
                    else:
                        prev_pos = hmap[word[idx]]
            idx += 1

        return True


object = Solution()
print(object.VerifyingAnAlienDictionary(["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"))
print(object.VerifyingAnAlienDictionary(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))
print(object.VerifyingAnAlienDictionary(["apple","app"], "abcdefghijklmnopqrstuvwxyz"))