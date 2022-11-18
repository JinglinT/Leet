class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:

        value = root.val
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if node.val != value:
                    return False
                stack.append(node.left)
                stack.append(node.right)

        return True
