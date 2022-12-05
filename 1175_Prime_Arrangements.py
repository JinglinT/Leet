class Solution:
    def numPrimeArrangements(self, n: int) -> int:

        def isPrime(num):
            for i in range(2, floor(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True

        countPrime = 0

        for num in range(2, n + 1):
            if isPrime(num):
                countPrime += 1

        return math.factorial(countPrime) * math.factorial(n - countPrime) % (10**9 + 7)
