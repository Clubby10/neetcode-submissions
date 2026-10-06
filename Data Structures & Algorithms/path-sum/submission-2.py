# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(n, curSum):
            if not n:
                return False

            curSum += n.val
            if n.left is None and n.right is None:
                return curSum == targetSum

            return dfs(n.left, curSum) or dfs(n.right, curSum)


        return dfs(root, 0)

            