# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if(root is None):
            return False
        if(self.helper(root,subRoot)):
            return True
        return (self.isSubtree(root.left,subRoot)
        or self.isSubtree(root.right,subRoot))


    def helper(self,root,subroot):
        if(root==None and subroot==None):
            return True
        if(root==None or subroot==None):
            return False
        if(root.val!=subroot.val):
            return False
        left=self.helper(root.left,subroot.left)
        right=self.helper(root.right,subroot.right)
        return (left and right)
        