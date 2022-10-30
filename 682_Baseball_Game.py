class Solution:
    def calPoints(self, operations: List[str]) -> int:

        res = []

        for ch in operations:
            if ch == '+':
                res.append(res[-1] + res[-2])
            elif ch == 'D':
                res.append(2 * res[-1])
            elif ch == 'C':
                res.pop()
            else:
                res.append(int(ch))

        return sum(res)
