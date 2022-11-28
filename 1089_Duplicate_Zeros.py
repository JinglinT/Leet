class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        countZeros = arr.count(0)
        newLen = len(arr) + countZeros

        i = len(arr) - 1
        j = newLen - 1

        while i > -1:

            if j < len(arr):
                arr[j] = arr[i]
            j -= 1

            if arr[i] == 0:
                if j < len(arr):
                    arr[j] = 0
                j -= 1

            i -= 1
