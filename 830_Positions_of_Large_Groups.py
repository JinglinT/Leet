class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:

        res = []

        i = 0
        j = 1

        while j < len(s) + 1:
            if j == len(s) or s[i] != s[j]:
                if j - i >= 3:
                    res.append([i, j - 1])
                i = j
            j += 1

        return res
