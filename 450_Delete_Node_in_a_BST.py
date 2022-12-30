class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        def deleteNode(root, val):
            if not root:
                return None

            if val == root.val:

                if not root.left:
                    return root.right
                if not root.right:
                    return root.left

                rightMinNode = findMinNode(root.right)

                root.right = deleteNode(root.right, rightMinNode.val)

                rightMinNode.left = root.left
                rightMinNode.right = root.right
                root = rightMinNode

            if val < root.val:
                root.left = deleteNode(root.left, val)
            else:
                root.right = deleteNode(root.right, val)

            return root

        def findMinNode(root):
            while root.left:
                root = root.left
            return root

        return deleteNode(root, key)
