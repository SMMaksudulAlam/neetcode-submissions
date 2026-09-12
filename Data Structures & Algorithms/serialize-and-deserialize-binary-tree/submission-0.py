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
                return "n"
            
            s = str(root.val)
            s += '_'+ser(root.left)
            s += '_'+ser(root.right)
            return s
        
        root_str = ser(root)
        return root_str
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split("_")
        ind = 0
        print(data)
        def build():
            nonlocal ind
            ch = data[ind]
            ind+=1
            if(ch == "n"):
                return None
            
            nde = TreeNode(int(ch))
            nde.left = build()
            nde.right = build()
            return nde
        
        root = build()
        return root








