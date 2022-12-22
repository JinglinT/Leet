class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def build(preStart, preEnd, inStart, inEnd):

            if preStart > preEnd:
                return None

            rootVal = preorder[preStart]

            inorderRootIndex = None
            for i in range(inStart, inEnd + 1):
                if inorder[i] == rootVal:
                    inorderRootIndex = i

            leftSubTreeSize = inorderRootIndex - inStart

            root = TreeNode(rootVal)

            root.left = build(preStart + 1, preStart +
                              leftSubTreeSize, inStart, inorderRootIndex - 1)
            root.right = build(preStart + leftSubTreeSize + 1,
                               preEnd, inorderRootIndex + 1, inEnd)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)
