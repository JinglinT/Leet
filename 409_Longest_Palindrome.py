class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        mid = 1
        count = collections.Counter(s)

        for c in count.values():
            if mid > 0:
                if c % 2 == 1:
                    res += 1
                    mid -= 1
            res += c // 2 * 2

        return res
