# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if root is None:
            return ans
        queue=deque()
        queue.append(root)
        #keep iterating while queue is empty
        while(queue):
            n=len(queue)
            level=[]
            for i in range(0,n):
                node=queue.popleft()
                level.append(node.val)
                if(node.left!=None):
                    queue.append(node.left)
                if(node.right!=None):
                    queue.append(node.right)
            ans.append(level)
        return ans
       