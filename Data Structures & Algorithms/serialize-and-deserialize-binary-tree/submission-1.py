# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        def ser(root):
            if(not root):
                return "N"
            s = str(root.val)
            s += "_"+ser(root.left)
            s += "_"+ser(root.right)
            return s
        return ser(root)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        q = deque(data.split("_"))
        def deser():
            nonlocal q
            val = q.popleft()
            if(val == "N"):
                return None
            root = TreeNode(int(val))
            root.left = deser()
            root.right = deser()
            return root
        return deser()

       








