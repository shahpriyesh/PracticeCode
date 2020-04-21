class SplitIntoBalanced:
    def splitIntoBalanced(self, s):
        L_cnt, R_cnt = 0, 0
        L_idx = 0
        result = []

        for idx in range(len(s)):
            if s[idx] is 'L':
                L_cnt += 1
            elif s[idx] is 'R':
                R_cnt += 1

            if L_cnt == R_cnt:
                result.append(s[L_idx: idx + 1])
                L_idx = idx + 1
        return len(result)


object = SplitIntoBalanced()
s = "LRLLLRRRRL"
print(object.splitIntoBalanced(s))