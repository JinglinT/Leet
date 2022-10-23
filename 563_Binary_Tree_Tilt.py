# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:

        res = 0

        def helper(root):
            if not root:
                return 0

            left_sum = helper(root.left)
            right_sum = helper(root.right)

            nonlocal res
            res += abs(left_sum - right_sum)

            return root.val + left_sum + right_sum

        helper(root)

        return res
