class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:

        dic = {}

        for i, v in enumerate(nums2):
            dic[v] = i

        res = []

        for n in nums1:
            res.append(dic[n])

        return res
