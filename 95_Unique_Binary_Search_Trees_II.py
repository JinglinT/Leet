class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        def helper(start, end):
            if start > end:
                return [None]

            res = []

            for i in range(start, end + 1):
                leftTrees = helper(start, i - 1)
                rightTrees = helper(i + 1, end)

                for left in leftTrees:
                    for right in rightTrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)

            return res

        return helper(1, n)
