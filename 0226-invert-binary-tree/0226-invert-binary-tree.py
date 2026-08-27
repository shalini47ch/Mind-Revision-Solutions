# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #this means left becomes right and right becomes left
        if root is None:
            return 
        root.left=self.invertTree(root.left)
        root.right=self.invertTree(root.right)
        #so here we do the swap
        root.left,root.right=root.right,root.left
        return root
        

       