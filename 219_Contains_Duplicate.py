class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            if hashset and len(hashset) == k:
                hashset.remove(nums[i - k])
            hashset.add(nums[i])

        return False
