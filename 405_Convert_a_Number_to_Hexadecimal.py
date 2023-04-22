class Solution:
    def toHex(self, num: int) -> str:

        if num == 0:
            return '0'

        res = []
        hex_map = "0123456789abcdef"

        if num < 0:
            num += (2 ** 32)

        while num:
            res.append(hex_map[num % 16])
            num //= 16

        res.reverse()

        return ''.join(res)
