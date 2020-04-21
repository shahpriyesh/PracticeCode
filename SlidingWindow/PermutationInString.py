from collections import Counter

class PermutationInString:
    def permutationInString(self, s1, s2):
        # length of string for which permutation to exist in s2 has to be smaller
        if len(s1) > len(s2):
            return False
        # all characters of s1 must be present in s2 in = or > amount
        s1Cnt = Counter(s1)
        s2Cnt = Counter(s2)
        # after subtraction if there still exist any character
        if len(s1Cnt - s2Cnt) > 0:
            return False
        return self.permute(list(s1), s2, 0, len(s1))

    def permute(self, l1, s2, start, end):
        if start >= end:
            return s2.find(''.join(l1)) != -1

        for i in range(start, end):
            l1[i], l1[start] = l1[start], l1[i]
            if self.permute(l1, s2, start+1, end):
                return True
            l1[i], l1[start] = l1[start], l1[i]

        return False


object = PermutationInString()
print(object.permutationInString("ab", "eidbaooo"))
print(object.permutationInString("ab", "eidboaoo"))
print(object.permutationInString("dinitrophenylhydrazine", "acetylphenylhydrazine"))
print(object.permutationInString("ab", "ba"))
s1 = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdef"
s2 = "bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefg"
print(object.permutationInString(s1, s2))