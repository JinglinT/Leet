class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        res = [None] * len(s)

        prev = float('-inf')

        for i in range(len(s)):
            if s[i] == c:
                prev = i
            res[i] = i - prev

        prev = float('inf')

        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i)

        return res
