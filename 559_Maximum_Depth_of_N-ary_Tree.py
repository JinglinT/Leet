"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def maxDepth(self, root: 'Node') -> int:

        res = 0
        stack = [(root, 1)]

        while stack:
            node, depth = stack.pop()
            if node:
                if not node.children and depth > res:
                    res = depth
                for child in node.children:
                    stack.append((child, depth + 1))

        return res
