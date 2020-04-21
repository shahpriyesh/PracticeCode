class LongestSubstrwoRepeatingChars:
    def __init__(self):
        pass

    def lengthOfLongestSubstring(self, s):
        dict = {}
        start = 0
        max_substr_len = 0

        for idx in range(len(s)):
            curr_ch = s[idx]

            # if this character hasn't been encountered yet, than simply add it in dictionary
            if curr_ch not in dict:
                dict[curr_ch] = idx
            # if this character has been encountered before than we need to modify start of substring
            else:
                # if this character is present in current substring that we are considering than update start position
                if dict[curr_ch] >= start:
                    start = dict[curr_ch] + 1
                # change location of character to point to last known index
                dict[curr_ch] = idx

            # calculate how long current string has been till now
            curr_substr_len = idx - start + 1
            max_substr_len = max(max_substr_len, curr_substr_len)

        return max_substr_len


object = LongestSubstrwoRepeatingChars()
print(object.lengthOfLongestSubstring("abcabcbb"))
print(object.lengthOfLongestSubstring("bbbbb"))
print(object.lengthOfLongestSubstring("pwwkew"))
print(object.lengthOfLongestSubstring("abba"))