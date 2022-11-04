class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def isPrime(n):
            if n == 1:
                return False
            for m in range(2, floor(math.sqrt(n)) + 1):
                if n % m == 0:
                    return False
            return True

        res = 0

        for n in range(left, right + 1):
            if isPrime(bin(n).count('1')):
                res += 1

        return res
