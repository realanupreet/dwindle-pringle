# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def sym(left: Optional[TreeNode], right: Optional[TreeNode]):
            if left is None or right is None:
                return left == right
            if left.val != right.val:
                return False
            return sym(left.left, right.right) and sym(left.right, right.left)
        return sym(root.left, root.right)
