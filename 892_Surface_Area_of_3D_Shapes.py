class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:

        n = len(grid)
        res = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    res += grid[i][j] * 4 + 2
                if i > 0:
                    res -= min(grid[i][j], grid[i - 1][j])
                if i < n - 1:
                    res -= min(grid[i][j], grid[i + 1][j])
                if j > 0:
                    res -= min(grid[i][j], grid[i][j - 1])
                if j < n - 1:
                    res -= min(grid[i][j], grid[i][j + 1])

        return res
