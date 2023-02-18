class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(0, numRows - 1):
            new = [1]
            for j in range(1, i + 1):
                new.append(res[i][j] + res[i][j - 1])
            new.append(1)
            res.append(new)
        return res
