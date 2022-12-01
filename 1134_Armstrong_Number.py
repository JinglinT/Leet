class Solution:
    def isArmstrong(self, n: int) -> bool:

        res = 0
        strN = str(n)

        for num in strN:
            res += int(num) ** len(strN)

        return res == n
