class Codec:

    def serialize(self, root):

        def helper(root):
            if not root:
                res.append('#')
                return

            res.append(str(root.val))

            helper(root.left)
            helper(root.right)

        res = []
        helper(root)

        return ','.join(res)

    def deserialize(self, data):

        def helper():
            rootVal = q.popleft()

            if rootVal == '#':
                return None

            root = TreeNode(int(rootVal))

            root.left = helper()
            root.right = helper()

            return root

        q = deque(data.split(','))

        return helper()
