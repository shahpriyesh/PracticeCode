from collections import Counter

class BuddyStrings:
    def buddyString(self, A, B):
        if len(A) != len(B):
            return False

        if A == B and len(set(A)) == 1:
            return True

        if Counter(A) != Counter(B):
            return False

        diff = 0
        for a, b in zip(A, B):
            if a != b:
                diff += 1
            if diff > 2:
                return False
        return True if diff == 2 else False


object = BuddyStrings()
print(object.buddyString("ab", "ba"))
print(object.buddyString("ab", "ab"))
print(object.buddyString("aa", "aa"))
print(object.buddyString("", "ba"))
print(object.buddyString("aaaaaaabc", "aaaaaaacb"))
print(object.buddyString("", ""))
print(object.buddyString("abcaa", "abcbb"))

# This returns False but should return True
print(object.buddyString("abab", "abab"))