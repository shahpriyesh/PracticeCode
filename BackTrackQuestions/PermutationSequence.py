class PermutationSequence:
    def permutationSequence(self, n, k):
        digits = [i for i in range(1, n+1)]
        cnt = [0]
        return ''.join([str(i) for i in self.permute(digits, k, cnt, 0, len(digits))])

    def permute(self, digits, k, cnt, start, end):
        if start == end:
            print(cnt[0], ": ", digits)
            cnt[0] += 1
            if cnt[0] == k:
                return digits
            else:
                return None

        for i in range(start, end):
            digits[i], digits[start] = digits[start], digits[i]
            if self.permute(digits, k, cnt, start+1, end):
                return digits
            digits[i], digits[start] = digits[start], digits[i]
        return None


object = PermutationSequence()
#print(object.permutationSequence(3, 3))
#print(object.permutationSequence(4, 9))
print(object.permutationSequence(3, 5))