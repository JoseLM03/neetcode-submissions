class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Return subtree height, or -1 if unbalanced
        def height(node):
            # Empty subtree has height 0
            if not node:
                return 0

            # Calculate the left subtree height
            left = height(node.left)
            if left == -1:
                return -1

            # Calculate the right subtree height
            right = height(node.right)
            if right == -1:
                return -1

            # Check if the height difference exceeds 1
            if abs(left - right) > 1:
                return -1

            # Return the height of this subtree
            return 1 + max(left, right)

        # True if the entire tree is balanced
        return height(root) != -1