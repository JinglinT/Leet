class Solution:
    def countLetters(self, s: str) -> int:

        res = 0

        curr = 1

        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                res += curr * (curr + 1) // 2
                curr = 0
            curr += 1

        res += curr * (curr + 1) // 2

        return res
