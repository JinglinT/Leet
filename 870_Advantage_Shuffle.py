class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nums1.sort(reverse=True)

        nums2_ = [(n, i) for i, n in enumerate(nums2)]
        nums2_.sort(reverse=True)

        res = [None] * len(nums1)

        left = 0
        right = len(nums1) - 1

        i = 0

        while i < len(nums2):
            if nums1[left] > nums2_[i][0]:
                res[nums2_[i][1]] = nums1[left]
                left += 1
            else:
                res[nums2_[i][1]] = nums1[right]
                right -= 1
            i += 1

        return res
