class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        count = [0] * 101

        for h in heights:
            count[h] += 1

        sortedHeight = []

        for i in range(len(count)):
            if count[i] > 0:
                sortedHeight += [i] * count[i]

        res = 0

        for i in range(len(heights)):
            if heights[i] != sortedHeight[i]:
                res += 1

        return res
