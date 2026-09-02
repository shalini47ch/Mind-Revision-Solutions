# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini=-sys.maxsize
        maxi=sys.maxsize
        return self.helper(root,mini,maxi)
    
    def helper(self,root,mini,maxi):
        if root is None:
            return True
        #now check for out of bound case
        if(root.val<=mini or root.val>=maxi):
            return False
        return (self.helper(root.left,mini,root.val)
        and self.helper(root.right,root.val,maxi))
        
        
        