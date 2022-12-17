class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        length = len(arr)

        for i in (length // 4, length // 2, length * 3 // 4, length - 1):
            if bisect_right(arr, arr[i]) - bisect_left(arr, arr[i]) > length // 4:
                return arr[i]
