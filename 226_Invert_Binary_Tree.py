class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root):
            if not root:
                return
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)

        helper(root)

        return root
