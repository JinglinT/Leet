class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 2, x // 2
        while left <= right:
            mid = (right + left) // 2
            if x == mid * mid:
                return mid
            if x < mid * mid:
                right = mid - 1
            else:
                left = mid + 1
        return right
