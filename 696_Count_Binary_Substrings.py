class Solution:
    def countBinarySubstrings(self, s: str) -> int:

        groups = []
        total = 0

        for i in range(len(s)):
            total += 1
            if i + 1 == len(s) or s[i + 1] != s[i]:
                groups.append(total)
                total = 0

        res = 0
        for i in range(len(groups) - 1):
            res += min(groups[i], groups[i + 1])

        return res
