class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:

        def build(i, j):
            if i > j:
                return None

            mx = float('-inf')
            mx_index = None

            for k in range(i, j + 1):
                if nums[k] > mx:
                    mx = nums[k]
                    mx_index = k

            node = TreeNode(mx)

            node.left = build(i, mx_index - 1)
            node.right = build(mx_index + 1, j)

            return node

        return build(0, len(nums) - 1)
