class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:

        m = len(img)
        n = len(img[0])

        res = [[0] * n for x in range(m)]

        for i in range(m):
            for j in range(n):
                count = 0
                for s_i in range(i - 1, i + 2):
                    for s_j in range(j - 1, j + 2):
                        if s_i > -1 and s_i < m and s_j > -1 and s_j < n:
                            res[i][j] += img[s_i][s_j]
                            count += 1
                res[i][j] //= count

        return res
