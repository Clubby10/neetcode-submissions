# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def preorder(n):
            if n is None:
                return None

            res.append(n.val)
            preorder(n.left)
            preorder(n.right)

        preorder(root)
        return res