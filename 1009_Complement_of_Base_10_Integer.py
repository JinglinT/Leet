class Solution:
    def bitwiseComplement(self, n: int) -> int:

        if n == 0:
            return 1

        length = 0
        m = n

        while m > 0:
            length += 1
            m = m >> 1

        return n ^ (2 ** length - 1)
