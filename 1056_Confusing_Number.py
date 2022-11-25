class Solution:
    def confusingNumber(self, n: int) -> bool:

        valid = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}

        m = n

        rotated = 0

        while m > 0:
            r = m % 10
            if r not in valid:
                return False
            rotated = rotated * 10 + valid[r]
            m //= 10

        return rotated != n
