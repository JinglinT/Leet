class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []

        def helper(root, path):
            if not root.left and not root.right:
                res.append(path)

            if root.left:
                copy_path = path[:]
                copy_path.append(str(root.left.val))
                helper(root.left, copy_path)
            if root.right:
                path.append(str(root.right.val))
                helper(root.right, path)

            return

        helper(root, [str(root.val)])

        res = ['->'.join(x) for x in res]

        return res
