class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:

        area_xy = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] > 0:
                    area_xy += 1

        area_xz = 0
        for row in grid:
            area_xz += max(row)

        area_zy = 0
        for j in range(len(grid[0])):
            largest = 0
            for i in range(len(grid)):
                largest = max(largest, grid[i][j])
            area_zy += largest

        return area_xy + area_xz + area_zy
