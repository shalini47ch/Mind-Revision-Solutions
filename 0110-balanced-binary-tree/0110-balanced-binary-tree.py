# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #absolute diff of lh,rh shouldnt be greater than 1 
        return self.helper(root)!=-1

    def helper(self,root):
        if root is None:
            return 0
        lh=self.helper(root.left)
        if(lh==-1):
            return -1
        rh=self.helper(root.right)
        if(rh==-1):
            return -1
        if(abs(lh-rh)>1):
            return -1
        return 1+max(lh,rh)
       