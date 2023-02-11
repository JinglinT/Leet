class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [(root, 1)]
        res = 0
        while stack:
            p, depth = stack.pop()
            if p:
                res = max(res, depth)
                stack.append((p.left, depth + 1))
                stack.append((p.right, depth + 1))
        return res
