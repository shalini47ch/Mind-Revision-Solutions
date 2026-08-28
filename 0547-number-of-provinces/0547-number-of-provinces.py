class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #here we need to return the no of provinces
        n=len(isConnected)
        visited=[0 for i in range(n)]
        adj=[[] for i in range(n)]
        #lets first build the graph first
        for i in range(0,n):
            for j in range(0,n):
                if(i!=j and isConnected[i][j]==1):
                    adj[i].append(j)
                    adj[j].append(i)
        count=0
        for i in range(0,n):
            if(visited[i]==0):
                count+=1
                self.dfs(i,visited,adj)
        return count 
    #now create a helper function to perform dfs
    def dfs(self,node,visited,adj):
        visited[node]=1
        for neigh in adj[node]:
            if(visited[neigh]==0):
                self.dfs(neigh,visited,adj)
       