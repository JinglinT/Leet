class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        res = float('inf')
        prev = None
        p = root
        stack = []

        while p or stack:
            while p:
                stack.append(p)
                p = p.left

            node = stack.pop()

            if prev != None and abs(prev - node.val) < res:
                res = abs(prev - node.val)
            prev = node.val

            p = node.right

        return res
