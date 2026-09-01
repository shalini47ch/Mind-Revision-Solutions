class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #this can be solved using the concept of bfs to solve this 
        m=len(heights)
        n=len(heights[0])
        pacificq=deque()
        pacificvisited=set()
        atlanticq=deque()
        atlanticvisited=set()
        #now iterate through the heights 
        for i in range(0,m):
            for j in range(0,n):
                if(i==0 or j==0):
                    pacificq.append((i,j))
                    pacificvisited.add((i,j))
                #now similarly do for atlantic as well
                if(i==m-1 or j==n-1):
                    atlanticq.append((i,j))
                    atlanticvisited.add((i,j))
        #now lets first do a bfs
        self.bfs(heights,pacificq,pacificvisited)
        self.bfs(heights,atlanticq,atlanticvisited)
        res=[]
        #now iterate again through the grid and if they are both in pacificvisited and atlanticvisited
        for i in range(0,m):
            for j in range(0,n):
                if((i,j) in pacificvisited and (i,j) in atlanticvisited):
                    res.append((i,j))
        return res 
    
    #now here create a helper to perform bfs
    def bfs(self,heights,queue,visited):
        n=len(heights)
        m=len(heights[0])
        #here the directions allowed are 4
        delrow=[-1,0,1,0]
        delcol=[0,1,0,-1]
        while(queue):
            ele=queue.popleft()
            r=ele[0]
            c=ele[1]
            for i in range(0,4):
                nrow=r+delrow[i]
                ncol=c+delcol[i]
                if(nrow>=0 and nrow<n and ncol>=0 and ncol<m and 
                (nrow,ncol) not in visited and heights[nrow][ncol]>=heights[r][c]):
                    queue.append((nrow,ncol))
                    visited.add((nrow,ncol))
        
       