class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Track the longest path found
        diameter = 0

        # Helper function calculates subtree heights
        def dfs(node):
            nonlocal diameter

            # Empty subtree has height 0
            if not node:
                return 0

            # Find the heights of both subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the longest path found
            diameter = max(diameter, left + right)

            # Return the height of the current subtree
            return 1 + max(left, right)

        # Start traversing from the root
        dfs(root)

        # Return the longest path in edges
        return diameter