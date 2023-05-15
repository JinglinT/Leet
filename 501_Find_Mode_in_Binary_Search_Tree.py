class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        prev = None
        curr_count = 0
        max_count = 0

        def helper(root):
            if not root:
                return
            helper(root.left)
            handleVal(root.val)
            helper(root.right)

        def handleVal(val):
            nonlocal res, prev, curr_count, max_count
            curr_count = curr_count + 1 if val == prev else 1
            if curr_count == max_count:
                res.append(val)
            elif curr_count > max_count:
                max_count = curr_count
                res = [val]
            prev = val

        helper(root)

        return res
