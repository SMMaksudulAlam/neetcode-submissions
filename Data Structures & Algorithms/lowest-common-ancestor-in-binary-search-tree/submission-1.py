# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ans = None

        def traverse(root):
            nonlocal ans
            if(not root):
                return 0

            left_count = traverse(root.left)
            if(left_count == 2):
                return 2
            right_count = traverse(root.right)
            if(right_count == 2):
                return 2

            if(root.val == p.val or root.val == q.val):
                if(left_count == 1 or right_count == 1):
                    ans = root
                    return 2
                else:
                    return 1

            if(left_count == 1 and right_count == 1):
                ans = root
                return 2

            return left_count + right_count

        count = traverse(root)
        return ans
