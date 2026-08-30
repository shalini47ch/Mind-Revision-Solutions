"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.hmap=defaultdict(int)
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        return self.helper(head)
    
    def helper(self,node):
        if node is None:
            return None 
        if node in self.hmap:
            return self.hmap[node]
        newnode=Node(node.val)
        self.hmap[node]=newnode
        newnode.next=self.helper(node.next)
        newnode.random=self.helper(node.random)
        return newnode
        