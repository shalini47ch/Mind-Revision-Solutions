#we need to connect the points so we will use dsu and to find minimum cost we will use minimum spanning tree to solve this 
class DisjointSet:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0 for i in range(n)]
    
    def findparent(self,node):
        if(node==self.parent[node]):
            return node 
        self.parent[node]=self.findparent(self.parent[node])
        return self.parent[node]
    
    def unionbyrank(self,u,v):
        upu=self.findparent(u)
        upv=self.findparent(v)
        if(upu==upv):
            return False
        if(self.rank[upu]<self.rank[upv]):
            self.parent[upu]=upv
        elif(self.rank[upv]<self.rank[upu]):
            self.parent[upv]=upu
        else:
            self.parent[upv]=upu
            self.rank[upu]+=1
        return True
        
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #now since we need to return the minimum cost to connect points we will use kruskals algo to solvet this 
        edges=[]
        n=len(points)
        for i in range(0,len(points)):
            for j in range(i+1,len(points)):
                #here use the formula of manhatten distance to solve this 
                cost=abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((cost,i,j))
        #now the next step is to sort on the basis of sort
        edges.sort(key=lambda x:x[0])
        mstsum=0
        ds=DisjointSet(n)
        for cost,u,v in edges:
            if(ds.unionbyrank(u,v)):
                mstsum+=cost
        return mstsum
        