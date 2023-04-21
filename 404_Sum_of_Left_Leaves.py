class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        valLeft = 0
        if root.left and not root.left.left and not root.left.right:
            valLeft = root.left.val

        sumLeft = self.sumOfLeftLeaves(root.left)
        sumRight = self.sumOfLeftLeaves(root.right)

        return valLeft + sumLeft + sumRight
