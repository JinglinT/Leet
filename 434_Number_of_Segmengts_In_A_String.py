class Solution:
    def countSegments(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            if s[i] != ' ' and (i + 1 == len(s) or s[i + 1] == ' '):
                res += 1

        return res
