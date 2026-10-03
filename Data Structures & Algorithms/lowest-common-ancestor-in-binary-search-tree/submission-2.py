# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def traverse(root, p, q):
            if(not root):
                return None
            if(p.val<=root.val<=q.val or q.val<=root.val<=p.val):
                return root
            if(p.val<root.val and q.val<root.val):
                return traverse(root.left, p, q)
            if(p.val>root.val and q.val>root.val):
                return traverse(root.right, p, q)
            return None

        return traverse(root, p, q)   
            