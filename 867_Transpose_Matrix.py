class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

        res = [[0] * len(matrix) for x in range(len(matrix[0]))]

        for i in range(len(res)):
            for j in range(len(res[i])):
                res[i][j] = matrix[j][i]

        return res
