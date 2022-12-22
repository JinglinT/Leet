class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        leftChild = root.left
        rightChild = root.right

        root.left = None
        root.right = leftChild

        p = root

        while p.right:
            p = p.right

        p.right = rightChild
