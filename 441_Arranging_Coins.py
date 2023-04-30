class Solution:
    def arrangeCoins(self, n: int) -> int:

        left = 1
        right = n

        while left <= right:
            mid = (left + right) // 2
            total = mid * (mid + 1) // 2
            if n == total:
                return mid
            if n < total:
                right = mid - 1
            else:
                left = mid + 1

        return right
