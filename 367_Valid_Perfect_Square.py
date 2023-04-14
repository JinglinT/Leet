class Solution(object):
    def isPerfectSquare(self, num):

        if num == 1:
            return True

        left = 2
        right = num // 2

        while left <= right:
            mid = (left + right) // 2
            if num == mid * mid:
                return True
            if num < mid * mid:
                right = mid - 1
            else:
                left = mid + 1

        return False
