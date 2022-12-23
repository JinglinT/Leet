class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:

        def helper(root):
            if not root:
                return '#'

            left = helper(root.left)
            right = helper(root.right)

            subTree = str(root.val) + ',' + left + ',' + right

            if subTree in count and count[subTree] == 1:
                res.append(root)

            count[subTree] = count.get(subTree, 0) + 1

            return subTree

        count = {}
        res = []
        helper(root)

        return list(res)
