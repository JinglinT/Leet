# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(root):
            nonlocal res
            if not root:
                return 0

            left_d = helper(root.left)
            right_d = helper(root.right)

            diameter = left_d + right_d
            if diameter > res:
                res = diameter

            return max(left_d, right_d) + 1

        helper(root)

        return res
