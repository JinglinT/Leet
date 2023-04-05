class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        if n < 1:
            return False

        return log(n, 3) % 1 == 0
