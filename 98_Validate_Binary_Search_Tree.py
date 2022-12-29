class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(root, low, high):
            if not root:
                return True

            if low != None and root.val <= low:
                return False
            if high != None and root.val >= high:
                return False

            left = helper(root.left, low, root.val)
            right = helper(root.right, root.val, high)

            return left and right

        return helper(root, None, None)
