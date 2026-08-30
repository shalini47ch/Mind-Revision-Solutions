class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #1s mean land and 0s mean water we need to return the no of islands 
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        count=0
        for i in range(0,n):
            for j in range(0,m):
                if(visited[i][j]==0 and grid[i][j]=="1"):
                    count+=1
                    self.dfs(i,j,visited,grid)
        return count 
    
    def dfs(self,row,col,visited,grid):
        n=len(grid)
        m=len(grid[0])
        visited[row][col]=1
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        for i in range(0,4):
            nrow=row+delrow[i]
            ncol=col+delcol[i]
            if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and 
            visited[nrow][ncol]==0 and grid[nrow][ncol]=="1"):
                self.dfs(nrow,ncol,visited,grid)


       