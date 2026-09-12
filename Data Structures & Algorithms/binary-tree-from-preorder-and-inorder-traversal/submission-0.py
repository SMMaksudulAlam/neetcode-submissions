# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        dic = {inorder[i]: i for i in range(len(inorder))}


        p_ind = 0
        def build(l_ind, r_ind):
            nonlocal p_ind
            if(l_ind>r_ind):
                return None
            nde = TreeNode(preorder[p_ind])
            in_ind = dic[preorder[p_ind]]
            p_ind+=1
            nde.left = build(l_ind, in_ind-1)
            nde.right = build(in_ind+1, r_ind)

            return nde
        
        return build(0, len(inorder)-1)
        

        