class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        def helper(root):
            if not root:
                return
            helper(root.left)

            nonlocal p
            root.left = None
            p.right = root
            p = p.right

            helper(root.right)

        dummy = p = TreeNode()

        helper(root)

        return dummy.right
