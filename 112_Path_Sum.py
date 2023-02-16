class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            p, total = stack.pop()
            if not p.left and not p.right and total == targetSum:
                return True
            if p.left:
                stack.append((p.left, p.left.val + total))
            if p.right:
                stack.append((p.right, p.right.val + total))
        return False
