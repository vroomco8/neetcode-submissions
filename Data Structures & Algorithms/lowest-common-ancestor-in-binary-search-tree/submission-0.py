# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def fs(node):
            if not node:
                return TreeNode()
            if node.val > p.val and node.val > q.val:
                return fs(node.left)
            elif node.val < p.val and node.val < q.val:
                return fs(node.right)
            else:
                return node

        return fs(root)
        