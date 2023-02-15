class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def helper(root):
            if not root:
                return 0, True
            leftHeight, leftIsBalanced = helper(root.left)
            if not leftIsBalanced:
                return 0, False
            rightHeight, rightIsBalanced = helper(root.right)
            if not rightIsBalanced:
                return 0, False
            if abs(leftHeight - rightHeight) > 1:
                return 0, False
            return 1 + max(leftHeight, rightHeight), True

        return helper(root)[1]
