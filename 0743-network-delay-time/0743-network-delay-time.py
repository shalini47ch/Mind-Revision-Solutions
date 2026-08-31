import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj=[[] for i in range(n+1)]
        #lets first build the graph
        for u,v,wt in times:
            adj[u].append((v,wt))
        dist=[sys.maxsize for i in range(n+1)]
        dist[k]=0
        minheap=[]
        heapq.heappush(minheap,[0,k])
        #the first is the distance and the second is the node 
        while(len(minheap)>0):
            ele=heapq.heappop(minheap)
            dis=ele[0]
            node=ele[1]
            for neigh in adj[node]:
                newnode=neigh[0]
                newwt=neigh[1]
                if(dis+newwt<dist[newnode]):
                    dist[newnode]=dis+newwt
                    heapq.heappush(minheap,[dist[newnode],newnode])
        ans=0
        for i in range(1,n+1):
            ans=max(ans,dist[i])
        return ans if ans!=sys.maxsize else -1

        
        