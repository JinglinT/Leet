class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:

        nums.sort()

        res = -1

        i = 0
        j = len(nums) - 1

        while i < j:
            total = nums[i] + nums[j]
            if total < k:
                res = max(res, total)
                i += 1
            else:
                j -= 1

        return res
