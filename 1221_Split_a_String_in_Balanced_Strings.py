class Solution:
    def balancedStringSplit(self, s: str) -> int:

        countR = countL = 0

        res = 0

        for ch in s:
            if ch == 'R':
                countR += 1
            else:
                countL += 1
            if countR == countL:
                res += 1

        return res
