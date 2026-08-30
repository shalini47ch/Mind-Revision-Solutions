"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.hmap=defaultdict(int)
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        return self.helper(node)
    
    def helper(self,node):
        if node is None:
            return None 
        if node in self.hmap:
            return self.hmap[node]
        newnode=Node(node.val)
        self.hmap[node]=newnode
        for neigh in node.neighbors:
            newnode.neighbors.append(self.helper(neigh))
        return newnode
        