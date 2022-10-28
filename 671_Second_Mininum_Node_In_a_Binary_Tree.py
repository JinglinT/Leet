class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return
            if root.val > min1 and root.val < self.res:
                self.res = root.val
            if root.val == min1:
                helper(root.left)
                helper(root.right)

        min1 = root.val
        self.res = float('inf')

        helper(root)

        return self.res if self.res < float('inf') else -1
