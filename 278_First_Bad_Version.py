class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            if right == 1:
                return 1

            mid = (left + right) // 2

            if isBadVersion(mid) and not isBadVersion(mid - 1):
                return mid

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return
