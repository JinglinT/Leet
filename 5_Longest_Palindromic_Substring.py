class Solution:
    def longestPalindrome(self, s: str) -> str:

        def Palindrome(i, j):
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]

        res = ''

        for i in range(len(s)):
            a = Palindrome(i, i)
            b = Palindrome(i, i + 1)
            res = max(res, a, b, key=lambda x: len(x))

        return res
