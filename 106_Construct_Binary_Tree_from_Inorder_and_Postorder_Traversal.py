class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(postStart, postEnd, inStart, inEnd):

            if postStart > postEnd:
                return None

            rootVal = postorder[postEnd]

            inorderRootIndex = None
            for i in range(inStart, inEnd + 1):
                if inorder[i] == rootVal:
                    inorderRootIndex = i

            leftSubTreeSize = inorderRootIndex - inStart

            root = TreeNode(rootVal)

            root.left = build(postStart, postStart + leftSubTreeSize -
                              1, inStart, inStart + leftSubTreeSize - 1)
            root.right = build(postStart + leftSubTreeSize,
                               postEnd - 1, inStart + leftSubTreeSize + 1, inEnd)

            return root

        return build(0, len(postorder) - 1, 0, len(inorder) - 1)
