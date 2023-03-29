class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        res = None
        minDiff = float('inf')

        while root:
            if root.val == target:
                return root.val

            diff = abs(root.val - target)

            if diff < minDiff:
                minDiff = diff
                res = root.val

            if target < root.val:
                root = root.left
            else:
                root = root.right

        return res
