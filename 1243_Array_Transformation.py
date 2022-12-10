class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:

        Change = True

        while Change:
            Change = False
            prev = arr[0]
            for i in range(1, len(arr) - 1):
                nextPrev = arr[i]
                if arr[i] < prev and arr[i] < arr[i + 1]:
                    arr[i] += 1
                    Change = True
                elif arr[i] > prev and arr[i] > arr[i + 1]:
                    arr[i] -= 1
                    Change = True
                prev = nextPrev

        return arr
