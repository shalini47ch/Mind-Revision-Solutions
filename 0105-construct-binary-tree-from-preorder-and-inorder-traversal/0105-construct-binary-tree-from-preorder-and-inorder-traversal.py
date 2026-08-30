# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #preorder is root left right and inorder is left root right
        n=len(inorder)
        m=len(preorder)
        return self.helper(0,n-1,inorder,0,m-1,preorder)

    def helper(self,instart,inend,inorder,prestart,preend,preorder):
        if(instart>inend or prestart>preend):
            return None
        root=TreeNode(preorder[prestart])
        ind=instart
        while(preorder[prestart]!=inorder[ind]):
            ind+=1
        count=ind-instart
        #now recursively move to left and right
        root.left=self.helper(instart,ind-1,inorder,prestart+1,prestart+count,preorder)
        #now do for right
        root.right=self.helper(ind+1,inend,inorder,prestart+count+1,preend,preorder)
        return root





    
       