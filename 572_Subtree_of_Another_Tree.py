# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def helper1(subRoot):
            if not subRoot:
                return [None]
            left = helper1(subRoot.left)
            right = helper1(subRoot.right)
            return left + [subRoot.val] + right

        def helper2(root):
            if not root:
                return [None]
            left = helper2(root.left)
            right = helper2(root.right)
            structure = left + [root.val] + right
            if root.val == subRoot.val and structure == substructure:
                nonlocal issubtree
                issubtree = True
            return structure

        issubtree = False
        substructure = helper1(subRoot)
        helper2(root)

        return issubtree
