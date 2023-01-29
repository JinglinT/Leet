class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        i = len(nums) - 1
        while k <= i:
            if nums[k] == val and nums[i] != val:
                nums[k], nums[i] = nums[i], nums[k]
            if nums[k] != val:
                k += 1
            if nums[i] == val:
                i -= 1
        return k
