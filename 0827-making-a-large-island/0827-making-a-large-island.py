#use the concept of disjoint set union to solve this 
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.size=[1 for i in range(n)]
    
    def findparent(self,node):
        if(node==self.parent[node]):
            return node 
        self.parent[node]=self.findparent(self.parent[node])
        return self.parent[node]
    
    #now create a helper function to perform unionbysize
    def unionbysize(self,u,v):
        upu=self.findparent(u)
        upv=self.findparent(v)
        if(upu==upv):
            return 
        if(self.size[upu]<self.size[upv]):
            self.parent[upu]=upv
            self.size[upv]+=self.size[upu]
        else:
            self.parent[upv]=upu
            self.size[upu]+=self.size[upv]
    
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        ds=DisjointSet(n*n)
        def cellno(r,c):
            #this gives the cell no
            return r*n+c 
        #here first step is to merge all 1's
        for i in range(0,n):
            for j in range(0,n):
                if(grid[i][j]==1):
                    #here directions are down and right
                    for dx,dy in [(1,0),(0,1)]:
                        newr=i+dx 
                        newc=j+dy
                        if(newr>=0 and newr<n and newc>=0 and newc<n and
                        grid[newr][newc]==1):
                           ds.unionbysize(cellno(i,j),cellno(newr,newc))
        #now do for largest island already exists
        ans=0
        for i in range(0,n):
            for j in range(0,n):
                if(grid[i][j]==1):
                    root=ds.findparent(cellno(i,j))
                    ans=max(ans,ds.size[root])
        #now try to replace every 0 with 1 and count
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        for i in range(0,n):
            for j in range(0,n):
                #here we will try to change 0's to 1's
                if(grid[i][j]==0):
                    count=1
                    seen=set()
                    for x in range(0,4):
                        nrow=i+delrow[x]
                        ncol=j+delcol[x]
                        if(nrow>=0 and nrow<n and ncol>=0 and ncol<n and 
                        grid[nrow][ncol]==1):
                            root=ds.findparent(cellno(nrow,ncol))
                            if root not in seen:
                                seen.add(root)
                                count+=ds.size[root]
                    ans=max(ans,count)
        return ans
                

                           




                           
        

        