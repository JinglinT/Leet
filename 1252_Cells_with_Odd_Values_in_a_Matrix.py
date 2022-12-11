class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:

        odd_rows, odd_cols, cntRow, cntCol = [False] * m, [False] * n, 0, 0
        for r, c in indices:
            odd_rows[r] ^= True
            odd_cols[c] ^= True
            cntRow += 1 if odd_rows[r] else -1
            cntCol += 1 if odd_cols[c] else -1
        return (n - cntCol) * cntRow + (m - cntRow) * cntCol
