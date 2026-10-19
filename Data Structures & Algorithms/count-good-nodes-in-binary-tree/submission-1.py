# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        gd = 0

        def dfs(root, mx):

            add = 0
            if not root:
                return 0
            if root.val >= mx:
                add += 1
            return add + dfs(root.left, max(root.val, mx)) + dfs(root.right, max(root.val, mx))
        return dfs(root, root.val)