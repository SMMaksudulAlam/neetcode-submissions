# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def traverse(root):
            if(not root):
                return True, 0
            
            l_okay, left = traverse(root.left)
            if(not l_okay):
                return False, 1 + l_okay
            r_okay, right = traverse(root.right)

            if(l_okay and r_okay and abs(left - right)<=1):
                return True, 1 + max(left, right)

            return False, 1 + max(left, right)
        
        ans, depth = traverse(root)
        return ans