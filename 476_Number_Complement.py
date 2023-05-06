class Solution:
    def findComplement(self, num: int) -> int:
        length = 0
        x = num

        while x > 0:
            length += 1
            x = x >> 1

        return num ^ (2 ** length - 1)
