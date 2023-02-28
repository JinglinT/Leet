class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        left = lower - 1
        for i in range(len(nums) + 1):
            right = nums[i] if i < len(nums) else upper + 1
            if right - left > 2:
                res.append(f'{left + 1}->{right - 1}')
            elif right - left == 2:
                res.append(f'{left + 1}')
            left = right
        return res
