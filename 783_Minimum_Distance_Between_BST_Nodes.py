class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:

        def helper(root):
            if not root:
                return
            helper(root.left)

            nonlocal prev
            nonlocal minDiff
            if prev != None:
                minDiff = min(minDiff, root.val - prev)
            prev = root.val

            helper(root.right)

        prev = None
        minDiff = float('inf')
        helper(root)

        return minDiff
