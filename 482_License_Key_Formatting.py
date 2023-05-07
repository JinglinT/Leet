class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        res = []
        count = 0

        for i in range(len(s) - 1, -1, -1):
            if count == k:
                res.append('-')
                count = 0
            if s[i] != '-':
                res.append((s[i]).upper())
                count += 1

        if res and res[len(res) - 1] == '-':
            res.pop()

        res.reverse()
        return ''.join(res)
