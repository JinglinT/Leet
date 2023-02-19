class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for i in range(rowIndex):
            new = [1]
            for j in range(1, i + 1):
                new.append(row[j] + row[j - 1])
            new.append(1)
            row = new

        return row
