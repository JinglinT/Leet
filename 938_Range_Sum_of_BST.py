class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        def helper(root):
            if not root:
                return
            helper(root.left)

            if low <= root.val <= high:
                self.res += root.val

            helper(root.right)

        self.res = 0
        helper(root)

        return self.res
