class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        stack = [root]
        res = []

        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                for i in range(len(node.children) - 1, -1, -1):
                    stack.append(node.children[i])

        return res
