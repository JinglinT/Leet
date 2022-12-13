class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        def reverse(row):
            i = 0
            j = len(row) - 1
            while i < j:
                row[i], row[j] = row[j], row[i]
                i += 1
                j -= 1

        n = len(matrix)

        for i in range(n):
            for j in range(n - i):
                matrix[i][j], matrix[n - j - 1][n - i -
                                                1] = matrix[n - j - 1][n - i - 1], matrix[i][j]

        for row in matrix:
            reverse(row)
