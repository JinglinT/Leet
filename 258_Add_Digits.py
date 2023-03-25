class Solution:
    def addDigits(self, num: int) -> int:

        def sumDigits(n):
            res = 0
            while n > 0:
                res += n % 10
                n //= 10
            return res

        while num // 10 != 0:
            num = sumDigits(num)

        return num
