class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:

        def helper(root, seq):
            if not root.left and not root.right:
                seq.append(root.val)
            if root.left:
                helper(root.left, seq)
            if root.right:
                helper(root.right, seq)

        seq1 = []
        seq2 = []
        helper(root1, seq1)
        helper(root2, seq2)

        return seq1 == seq2
