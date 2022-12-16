class Solution:
    def subtractProductAndSum(self, n: int) -> int:

        total = 0
        product = 1

        while n > 0:
            r = n % 10
            total += r
            product *= r
            n //= 10

        return product - total
