# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #serialization means we need to do it in comma separated form so lets use the preorder traversal concept
        ans=[]
        self.helper(root,ans)
        return ",".join(ans)


    
    def helper(self,root,ans):
        if root is None:
            ans.append("null")
            return 
        #root left right
        ans.append(str(root.val))
        self.helper(root.left,ans)
        self.helper(root.right,ans)
       
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        arr=data.split(",")
        return self.dep(arr)
    
    def dep(self,arr):
        if not arr:
            return None
        val=arr.pop(0)
        if(val=="null"):
            return None
        root=TreeNode(int(val))
        root.left=self.dep(arr)
        root.right=self.dep(arr)
        return root

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))