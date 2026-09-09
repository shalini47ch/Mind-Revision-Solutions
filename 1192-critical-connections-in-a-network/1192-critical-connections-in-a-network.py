class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        #so here the critical connections are basically the bridges of the graph so we will use the concept of tarjans algo with a condition of low[neigh]>low[node] to find bridges
        graph=[[] for i in range(n)]
        #we have an undirected graph
        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)
        dis=[-1 for i in range(n)]
        low=[-1 for i in range(n)]
        timer=0
        bridges=[]
        def dfs(node,parent):
            nonlocal timer
            dis[node]=timer
            low[node]=timer
            timer+=1
            #now check for the neigh 
            for neigh in graph[node]:
                if(neigh==parent):
                    continue
                #if already visited case
                if(dis[neigh]==-1):
                    dfs(neigh,node)
                    low[node]=min(low[node],low[neigh])
                    if(low[neigh]>dis[node]):
                        #means the case for bridge
                        bridges.append([node,neigh])
                else:
                    low[node]=min(low[node],dis[neigh])
        for node in range(n):
            if(dis[node]==-1):
                dfs(node,-1)
        return bridges
                


        