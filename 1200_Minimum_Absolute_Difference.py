class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        arr.sort()

        minD = float('inf')

        for i in range(len(arr) - 1):
            minD = min(minD, abs(arr[i] - arr[i + 1]))

        res = []

        for i in range(len(arr) - 1):
            if abs(arr[i] - arr[i + 1]) == minD:
                res.append([arr[i], arr[i + 1]])

        return res
