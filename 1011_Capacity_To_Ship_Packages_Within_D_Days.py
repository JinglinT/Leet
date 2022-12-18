class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            total = 0
            need_days = 1

            for w in weights:
                if total + w > mid:
                    need_days += 1
                    total = 0
                total += w

            if need_days <= days:
                right = mid - 1
            else:
                left = mid + 1

        return left
