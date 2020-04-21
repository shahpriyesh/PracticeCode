class LongestSubstrWithKRepeatingChars:
    def longestSubstrWithKRepeatingChars(self, s, K):
        dict = {}
        dict_cnt = 0
        curr_len = 0
        start_idx = 0

        for idx in range(len(s)):
            if s[idx] not in dict:
                if dict_cnt < 3:
                    dict[s[idx]] = idx
                    dict_cnt += 1
                else:
                    # find the minimum and maximum value key in dictionary
                    min_key = min(dict, key=dict.get)
                    max_key = max(dict, key=dict.get)

                    # see if answer till now's length is lesser than answer we just found
                    if curr_len < dict[max_key] - start_idx:
                        curr_len = dict[max_key] - start_idx

                    # Reset start_idx to current idx
                    start_idx = dict[min_key] + 1
                    # Remove key with minimum value
                    dict.pop(min_key)
                    # Now add new key in dictionary
                    dict[s[idx]] = idx
            else:
                dict[s[idx]] = idx

        # Finally check final answer
        # find the minimum and maximum value key in dictionary
        min_key = min(dict, key=dict.get)
        max_key = max(dict, key=dict.get)

        # see if answer till now's length is lesser than answer we just found
        if curr_len < dict[max_key] - start_idx:
            curr_len = dict[max_key] - start_idx

        return curr_len


object = LongestSubstrWithKRepeatingChars()
s = "aaabb"
k = 3
print(object.longestSubstrWithKRepeatingChars(s, k))