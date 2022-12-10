class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:

        slope = None

        if coordinates[0][1] - coordinates[1][1] == 0:
            slope = float('inf')
        else:
            slope = (coordinates[0][0] - coordinates[1][0]) / \
                (coordinates[0][1] - coordinates[1][1])

        for i in range(1, len(coordinates) - 1):
            curr_slope = None
            if coordinates[i][1] - coordinates[i + 1][1] == 0:
                curr_slope = float('inf')
            else:
                curr_slope = (coordinates[i][0] - coordinates[i + 1]
                              [0]) / (coordinates[i][1] - coordinates[i + 1][1])
            if curr_slope != slope:
                return False

        return True
