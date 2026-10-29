class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Check whether two trees are identical
        def same(p, q):
            # Both nodes are empty, so they match
            if not p and not q:
                return True

            # Only one node is empty, so they differ
            if not p or not q:
                return False

            # Different node values mean different trees
            if p.val != q.val:
                return False

            # Both left and right subtrees must match
            return (
                same(p.left, q.left)
                and same(p.right, q.right)
            )

        # An empty subRoot is always a valid subtree
        if not subRoot:
            return True

        # Search for a matching subtree
        def search(node):
            # No more nodes to search
            if not node:
                return False

            # Check if this entire subtree matches
            if same(node, subRoot):
                return True

            # Otherwise, search both children
            return search(node.left) or search(node.right)

        # Begin searching from the root
        return search(root)