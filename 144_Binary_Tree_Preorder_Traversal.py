class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = [root]
        res = []
        while stack:
            p = stack.pop()
            if p:
                res.append(p.val)
                stack.append(p.right)
                stack.append(p.left)
        return res
