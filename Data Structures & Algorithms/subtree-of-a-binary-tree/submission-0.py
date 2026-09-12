# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def ser(root, s):
            if(not root):
                return s+"_"+"n"
            
            s = s + "_"+ str(root.val)
            s = ser(root.left, s)
            s = ser(root.right, s)
            return s
        
        root_str = ser(root, "")
        sub_root_str = ser(subRoot, "")
        if(sub_root_str in root_str):
            return True
        return False

        


            