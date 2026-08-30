class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #here we need to return the maximum area of the island
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        maxarea=0
        #traverse through the grid 
        for i in range(0,n):
            for j in range(0,m):
                if(visited[i][j]==0 and grid[i][j]==1):
                    maxarea=max(maxarea,self.bfs(i,j,visited,grid))
        return maxarea 
    
    def bfs(self,row,col,visited,grid):
        n=len(grid)
        m=len(grid[0])
        area=0
        queue=deque()
        queue.append((row,col))
        visited[row][col]=1
        area+=1
        #now we are allowed to move in 4 directions 
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while(queue):
            ele=queue.popleft()
            r=ele[0]
            c=ele[1]
            for x in range(0,4):
                nrow=r+delrow[x]
                ncol=c+delcol[x]
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and 
                visited[nrow][ncol]==0 and grid[nrow][ncol]==1):
                    queue.append((nrow,ncol))
                    visited[nrow][ncol]=1
                    area+=1
        return area
       