class Solution:
    def fixedPoint(self, arr: List[int]) -> int:

        res = None

        left = 0
        right = len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == mid:
                res = mid
                right = mid - 1
            if arr[mid] < mid:
                left = mid + 1
            else:
                right = mid - 1

        return -1 if res == None else res
