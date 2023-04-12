class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        count1 = collections.Counter(nums1)
        res = []

        for n in nums2:
            if n in count1 and count1[n] > 0:
                res.append(n)
                count1[n] -= 1

        return res
