class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        left = 0

        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i + 1] - nums[i] > 1:
                if nums[left] != nums[i]:
                    res.append(f'{nums[left]}->{nums[i]}')
                else:
                    res.append(f'{nums[left]}')
                left = i + 1

        return res
