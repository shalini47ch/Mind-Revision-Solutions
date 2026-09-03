class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        #we will use dijkstra algorithm to solve this 
        n=len(grid)
        m=len(grid[0])
        visited=[[0 for i in range(m)]for j in range(n)]
        minheap=[]
        heapq.heappush(minheap,[grid[0][0],[0,0]])
        #the first is the time and the other is row,col
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while(len(minheap)>0):
            ele=heapq.heappop(minheap)
            currtime=ele[0]
            r=ele[1][0]
            c=ele[1][1]
            if(r==n-1 and c==m-1):
                return currtime
            #now checking for the neighbor nodes
            for x in range(0,4):
                nrow=r+delrow[x]
                ncol=c+delcol[x]
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and
                visited[nrow][ncol]==0):
                   time=max(grid[nrow][ncol],currtime)
                   #now push in the queue and mark as visited
                   heapq.heappush(minheap,[time,[nrow,ncol]])
                   visited[nrow][ncol]=1
        return 0

       