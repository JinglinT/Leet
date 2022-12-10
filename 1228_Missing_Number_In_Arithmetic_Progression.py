class Solution:
    def missingNumber(self, arr: List[int]) -> int:

        gap = (arr[-1] - arr[0]) // len(arr)

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == arr[0] + gap * mid:
                left = mid + 1
            else:
                right = mid - 1

        return arr[right] + gap
