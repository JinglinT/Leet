class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        def build(preStart, preEnd, postStart, postEnd):

            if preStart > preEnd:
                return None

            if preStart == preEnd:
                return TreeNode(preorder[preStart])

            rootVal = preorder[preStart]

            postOrderLeftRootIndex = None
            for i in range(len(postorder)):
                if postorder[i] == preorder[preStart + 1]:
                    postOrderLeftRootIndex = i

            leftSubTreeSize = postOrderLeftRootIndex - postStart + 1

            root = TreeNode(rootVal)

            root.left = build(preStart + 1, preStart +
                              leftSubTreeSize, postStart, postOrderLeftRootIndex)
            root.right = build(preStart + leftSubTreeSize + 1,
                               preEnd, postOrderLeftRootIndex + 1, postEnd - 1)

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)
