# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        #here we will use the concept of dfs to solve this 
        self.maxi=-sys.maxsize
        #there are two options either we can include the root or exclude the root
        def dfs(node):
            if not node:
                return 0
            left=max(0,dfs(node.left))
            right=max(0,dfs(node.right))
            self.maxi=max(self.maxi,node.val+left+right)
            return node.val+max(left,right)
        dfs(root)
        return self.maxi
        
   

       