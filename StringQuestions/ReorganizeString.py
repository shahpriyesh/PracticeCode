from collections import Counter

class ReorganizeString:
    def reorganizeString_INCORRECT(self, S):
        S = list(S)
        S.sort()
        right = len(S)-1
        left = 0
        while left < right:
            # are two adjacent characters same?
            if S[left] == S[left+1]:
                # is left side replacement candidate = (left+1)th char, same as right side replacement candidate right?
                if S[left+1] == S[right]:
                    # skip the right candidate as it can't be replaced here, move right pointer one position left
                    right -= 1
                else:
                    # yes we can swap these two chars, so that left and left+1 becomes different
                    S[left+1], S[right] = S[right], S[left+1]
                    # string is fixed up to left, now move ahead
                    left += 1
            else:
                # huh, nothing to do as chars are already different
                left += 1
        for i in range(len(S)-1):
            if S[i] == S[i+1]:
                return ''
        return ''.join(S)

    def reorganizeString(self, S):
        # if there is only single char
        if len(S) <= 1:
            return S

        # Count occurences of each char
        cntr = Counter(S)
        # if there is only single type of character
        if len(cntr) <= 1:
            return ''

        # Find out maximum to minimum occuring chars
        mc = cntr.most_common()

        res = []

        # take the highest count element as candidate and second highest as replacer
        candidate_cnt = 0
        replacer_cnt = 0

        # if there are still elements left
        while mc:
            # if the cnt is zero, pop and use as candidate
            if candidate_cnt == 0:
                item = mc.pop(0)
                candidate = item[0]
                candidate_cnt = item[1]

            # no more replacer left, than break
            if not mc:
                break

            # if the cnt is zero, pop and use as replacer
            if replacer_cnt == 0:
                item = mc.pop(0)
                replacer = item[0]
                replacer_cnt = item[1]

            res.append(candidate)
            res.append(replacer)

            candidate_cnt -= 1
            replacer_cnt -= 1

        while replacer_cnt > 0:
            res.append(candidate)
            res.append(replacer)

            candidate_cnt -= 1
            replacer_cnt -= 1

        if candidate_cnt != 0:
            if candidate_cnt != 1:
                return ""
            else:
                res.append(candidate)

        return ''.join(res)



object = ReorganizeString()
print(object.reorganizeString("aab"))
print(object.reorganizeString("aaab"))
print(object.reorganizeString("aaaaa"))
print(object.reorganizeString("aabbbbaa"))

print(object.reorganizeString("bfrbs"))

print(object.reorganizeString("eweweweweweweweweweweweweweueueueueueueueueueueueueueueuhuhuhuhuhuhshshshshshshshshshshshshshshshshshshshphphphpcpcpcpcpcpcpcpcpcpcpcpcpcpcpcrcrcrcrcrcrcrcrcrcrcrcrmrmrmrmrmrmrmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmxmgmgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvgvovovovovovovovovonononononononononbnbnbnbnbnbnbnbnbnbnbnbnbnbnbabaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiaiatatatatatftftftftftftftftftftftfdfdfdfdfdfdfdfdfdfdfdydydydydyzyzyzyzyzyzyzyzyzyzyzyzyzyzyjyjyjyjkjkjkjkjkjkjkjklklklklklklklklklklklkqkqkqwqwqwqwqwqwqwqwq"))