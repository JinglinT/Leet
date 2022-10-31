class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        while root and root.val != val:
            if val < root.val:
                root = root.left
            else:
                root = root.right

        return root
