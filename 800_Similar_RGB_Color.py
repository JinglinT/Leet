class Solution:
    def similarRGB(self, color: str) -> str:

        def minDiffShortHand(hexadecimal):
            minDiff = float('inf')
            res = None
            for n in range(16):
                diff = (int(hexadecimal, 16) - n * 17) ** 2
                if diff < minDiff:
                    minDiff = diff
                    res = n
            return hex(res)[-1] * 2

        res = '#'

        for i in range(1, len(color), 2):
            res += minDiffShortHand(color[i: i + 2])

        return res
