class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m = len(grid)
        n = len(grid[0])

        res = [[0] * n for i in range(m)]

        for i in range(m):
            for j in range(n):
                total = j + k
                newRow = (i + total // n) % m
                newCol = total % n
                res[newRow][newCol] = grid[i][j]

        return res
