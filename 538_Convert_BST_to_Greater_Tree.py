class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def helper(root):
            if not root:
                return
            helper(root.right)

            nonlocal total
            total += root.val
            root.val = total

            helper(root.left)

        total = 0

        helper(root)

        return root
