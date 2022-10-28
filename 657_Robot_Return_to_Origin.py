class Solution:
    def judgeCircle(self, moves: str) -> bool:

        vertical = {'R': 1, 'L': -1}
        horizontal = {'U': 1, 'D': -1}
        v = 0
        h = 0

        for m in moves:
            if m in vertical:
                v += vertical[m]
            else:
                h += horizontal[m]

        return v == 0 and h == 0
