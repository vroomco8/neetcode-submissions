# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if root is None:
            return []

        q = []
        res = []

        q.append(root)
        lvl = 0

        while q:
            ln = len(q)
            res.append([])

            for i in range(ln):
                node = q.pop(0)
                res[lvl].append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            lvl += 1
        print(res)
        fin = [x[-1] for x in res]

        return fin
        