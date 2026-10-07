"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        #DFS
        mp = {} # level -> node

        def dfs(node, level):
            if not node:
                return

            if level not in mp:
                mp[level] = node
            else:
                mp[level].next = node
                mp[level] = node

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return root