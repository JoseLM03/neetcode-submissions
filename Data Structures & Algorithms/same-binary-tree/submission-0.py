class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both trees are empty, so they match
        if not p and not q:
            return True

        # Only one tree is empty, so they differ
        if not p or not q:
            return False

        # Their current node values must match
        if p.val != q.val:
            return False

        # Compare the left subtrees AND compare the right subtrees
        return (
            self.isSameTree(p.left, q.left)
            and self.isSameTree(p.right, q.right)
        )