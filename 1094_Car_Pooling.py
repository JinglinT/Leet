class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        lastDrop = max(trips, key=lambda x: x[2])[2]

        diff = [0] * lastDrop

        for trip in trips:
            diff[trip[1]] += trip[0]
            if trip[2] < len(diff):
                diff[trip[2]] -= trip[0]

        for i in range(len(diff)):
            if i > 0:
                diff[i] = diff[i - 1] + diff[i]
            if diff[i] > capacity:
                return False

        return True
