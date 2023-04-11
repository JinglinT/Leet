class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        hashset = set(nums1)

        for n in nums2:
            if n in hashset:
                res.add(n)

        return list(res)
