class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        queue = collections.deque()

        queue.append((root, 0))
        level = 0
        total = 0
        count = 0
        res = []

        while queue:
            node, lvl = queue.popleft()

            if lvl == level:
                total += node.val
                count += 1
            else:
                res.append(total / count)
                total = node.val
                count = 1
                level = lvl

            if node.left:
                queue.append((node.left, lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))

        res.append(total / count)

        return res
