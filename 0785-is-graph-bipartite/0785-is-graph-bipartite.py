class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        #here we need to make sure adjancent nodes shouldnt have the same color
        n=len(graph)
        color=[-1 for i in range(n)]
        for i in range(0,n):
            if(color[i]==-1):
                #node,color,graph and currcolor
                if(self.dfs(i,color,graph,1)==False):
                    return False
        return True
    
    #now here create a helper function to perform dfs 
    def dfs(self,node,color,graph,currcolor):
        color[node]=currcolor
        #check for the neigh nodes
        for neigh in graph[node]:
            if(color[neigh]==color[node]):
                return False
            newcolor=1-currcolor
            if(color[neigh]==-1):
                if(self.dfs(neigh,color,graph,newcolor)==False):
                    return False
        return True




        