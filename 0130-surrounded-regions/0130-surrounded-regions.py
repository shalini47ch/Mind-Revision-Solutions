class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        for j in range(0,m):
            if(visited[0][j]==0 and grid[0][j]=="O"):
                self.dfs(0,j,visited,grid)
            if(visited[n-1][j]==0 and grid[n-1][j]=="O"):
                self.dfs(n-1,j,visited,grid)
        #now do for 1st col last col
        for i in range(0,n):
            if(visited[i][0]==0 and grid[i][0]=="O"):
                self.dfs(i,0,visited,grid)
            if(visited[i][m-1]==0 and grid[i][m-1]=="O"):
                self.dfs(i,m-1,visited,grid)
        #now at last we do replace
        for i in range(0,n):
            for j in range(0,m):
                if(visited[i][j]==0 and grid[i][j]=="O"):
                    grid[i][j]="X"
        return grid
    
    def dfs(self,r,c,visited,grid):
        n=len(grid)
        m=len(grid[0])
        visited[r][c]=1
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        for i in range(0,4):
            nrow=r+delrow[i]
            ncol=c+delcol[i]
            if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and 
            visited[nrow][ncol]==0 and grid[nrow][ncol]=="O"):
                self.dfs(nrow,ncol,visited,grid)
       