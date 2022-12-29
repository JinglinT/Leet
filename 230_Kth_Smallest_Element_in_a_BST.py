class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def helper(root):
            if not root:
                return
            helper(root.left)

            nonlocal k, res
            if k == 1:
                res = root.val
            k -= 1

            helper(root.right)

        res = None

        helper(root)

        return res
