class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left <= right:
            mid = (left + right) // 2

            total = 0
            need_count = 1

            for n in nums:
                if total + n > mid:
                    need_count += 1
                    total = 0
                total += n

            if need_count <= k:
                right = mid - 1
            else:
                left = mid + 1

        return left
