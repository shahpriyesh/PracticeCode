class RemovePalindromicSubsequence:
    def removePalindromicSubsequence(self, s):
        return 0 if s == "" else (1 if s == s[::-1] else 2)

'''
1332 -> Remove palindromic subsequences
- Observe: you are asked for subsequence (can be non-continuous) not subarray (continuous).
Observe: the string only contains 2 distinct characters 'a' and 'b'.
if str is empty => return 0, if str is palindrome => return 1,
otherwise return 2. where 1 step to remove all 'a's and another for all 'b's
'''