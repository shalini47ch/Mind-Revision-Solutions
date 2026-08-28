from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        queue=deque()
        for i in range(0,n):
            for j in range(0,m):
                if(grid[i][j]==2):
                    queue.append([[i,j],0])
                    visited[i][j]=2
        timer=0
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while(queue):
            ele=queue.popleft()
            r=ele[0][0]
            c=ele[0][1]
            time=ele[1]
            timer=max(timer,time)
            for i in range(0,4):
                nrow=r+delrow[i]
                ncol=c+delcol[i]
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and
                visited[nrow][ncol]!=2 and grid[nrow][ncol]==1):
                    queue.append([[nrow,ncol],time+1])
                    visited[nrow][ncol]=2
        for i in range(0,n):
            for j in range(0,m):
                if(visited[i][j]!=2 and grid[i][j]==1):
                    return -1
        return timer


        