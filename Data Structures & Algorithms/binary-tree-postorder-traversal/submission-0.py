# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def postorder(n):
            if n is None:
                return None

            postorder(n.left)
            postorder(n.right)
            res.append(n.val)

        postorder(root)
        return res