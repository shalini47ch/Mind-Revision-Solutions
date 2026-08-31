import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #we will use the concept of dijkstra to solve this 
        adj=[[] for i in range(n)]
        for u,v,wt in flights:
            adj[u].append((v,wt))
        dist=[sys.maxsize for i in range(n)]
        dist[src]=0
        minheap=[]
        #here we will store stops node and the distance
        heapq.heappush(minheap,[0,[src,0]])
        while(len(minheap)>0):
            ele=heapq.heappop(minheap)
            stops=ele[0]
            node=ele[1][0]
            dis=ele[1][1]
            for neigh in adj[node]:
                newnode=neigh[0]
                newwt=neigh[1]
                if(dis+newwt<dist[newnode] and stops<=k):
                    #so here we update the distance
                    dist[newnode]=dis+newwt
                    heapq.heappush(minheap,[stops+1,[newnode,dist[newnode]]])
        if(dist[dst]==sys.maxsize):
            return -1
        return dist[dst]

      