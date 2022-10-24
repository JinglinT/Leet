class Solution:
    def findLHS(self, nums: List[int]) -> int:

        c = collections.Counter(nums)
        res = 0

        for k in c.keys():
            if k + 1 in c:
                res = max(res, c[k] + c[k + 1])

        return res
