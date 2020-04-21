class LongestPalindromicSubsequence:
    max_len = 0
    start = 0

    def __init__(self):
        max_len = 0
        start = 0

    # https://leetcode.com/problems/longest-palindromic-substring/discuss/2928/Very-simple-clean-java-solution
    def longestPalindromicSubsequence(self, s):
        if len(s) < 2:
            return s

        for idx in range(len(s)):
            # for odd length palindrome
            self.__extendPalindrome(s, idx, idx)
            # for even length palindrome
            self.__extendPalindrome(s, idx, idx+1)

        response = s[self.start : self.start + self.max_len]
        return response

    def __extendPalindrome(self, s, j, k):
        while j >= 0 and k < len(s) and s[j] == s[k]:
            # move leftward
            j = j - 1
            # move rightward
            k = k + 1

        # Here we found a palindrome substring that is between j+1 to k
        curr_len = k - j - 1
        if curr_len > self.max_len:
            self.max_len = curr_len
            self.start = j+1

    # https://leetcode.com/problems/longest-palindromic-substring/discuss/151144/Bottom-up-DP-Logical-Thinking
    def longestPalindromicSubsequence_DP(self, s):
        str_len = len(s)
        result_length = 1
        result_start = 0

        # single char string is longest palindrome
        if str_len <= 1:
            return s

        # create storage matrix for bottom up DP
        dp = [[0 for i in range(str_len)] for j in range(str_len)]

        # single chars are always palindromes
        for i in range(str_len):
            dp[i][i] = 1

        # double chars has to be checked as special case
        for i in range(str_len - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
                result_start = i
                result_length = 2

        for start in range(str_len - 1, 0, -1):
            for dist in range(1, str_len - start):
                end = dist + start
                if dist == 1:
                    dp[start][end] = (s[start] == s[end])
                else:
                    dp[start][end] = ((s[start] == s[end]) and (dp[start + 1][end - 1]))

                if dp[start][end] and end - start + 1 > result_length:
                    result_length = end - start + 1
                    result_start = start

        return s[result_start : result_start + result_length]


#object = LongestPalindromicSubsequence()
#print(object.longestPalindromicSubsequence("bananas"))
#object = LongestPalindromicSubsequence()
#print(object.longestPalindromicSubsequence("bb"))

#object = LongestPalindromicSubsequence()
#print(object.longestPalindromicSubsequence_DP("bananas"))
#object = LongestPalindromicSubsequence()
#print(object.longestPalindromicSubsequence_DP("bb"))

# NOT WORKING
object = LongestPalindromicSubsequence()
print(object.longestPalindromicSubsequence_DP("ccc"))