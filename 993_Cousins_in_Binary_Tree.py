class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:

        parent = None
        depth = None

        stack = [(root, None, 0)]

        while stack:
            node, p, d = stack.pop()

            if node:

                if node.val == x or node.val == y:
                    if not depth:
                        parent = p
                        depth = d
                    else:
                        return parent != p and depth == d

                stack.append((node.left, node.val, d + 1))
                stack.append((node.right, node.val, d + 1))
