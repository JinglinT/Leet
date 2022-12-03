class Solution:
    def tribonacci(self, n: int) -> int:

        if n < 2:
            return n
        if n == 2:
            return 1

        res = 0
        a = 0
        b = 1
        c = 1

        for i in range(n - 2):
            res = a + b + c
            a = b
            b = c
            c = res

        return res
