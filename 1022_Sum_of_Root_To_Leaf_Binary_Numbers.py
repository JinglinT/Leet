class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def helper(root, v):
            v = v * 2 + root.val
            if not root.left and not root.right:
                self.res += v
                return
            if root.left:
                helper(root.left, v)
            if root.right:
                helper(root.right, v)

        self.res = 0

        helper(root, 0)

        return self.res
