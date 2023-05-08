class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        count = 0

        for n in nums:
            if n == 1:
                count += 1
            else:
                count = 0
            if count > maximum:
                maximum = count

        return maximum
