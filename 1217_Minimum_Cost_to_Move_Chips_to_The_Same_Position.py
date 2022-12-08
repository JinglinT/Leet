class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:

        oddSum = evenSum = 0

        for i in position:
            if i % 2 == 1:
                oddSum += 1
            else:
                evenSum += 1

        return min(oddSum, evenSum)
