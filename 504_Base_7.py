class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0:
            return '0'

        res = []
        n = abs(num)

        while n > 0:
            res.append(n % 7)
            n //= 7

        return '-' * (num < 0) + ''.join(str(x) for x in res[::-1])
