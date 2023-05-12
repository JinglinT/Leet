class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        m = {}

        for n in nums2:
            while stack and n > stack[len(stack) - 1]:
                m[stack.pop()] = n
            stack.append(n)

        while stack:
            m[stack.pop()] = -1

        res = []

        for n in nums1:
            res.append(m[n])

        return res
