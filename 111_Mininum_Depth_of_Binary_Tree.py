class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stack = ([(root, 1)])
        result = float('inf')
        while stack:
            p, depth = stack.pop()
            if p and not p.left and not p.right:
                result = min(result, depth)
            if p:
                stack.append((p.left, depth + 1))
                stack.append((p.right, depth + 1))
        return result
