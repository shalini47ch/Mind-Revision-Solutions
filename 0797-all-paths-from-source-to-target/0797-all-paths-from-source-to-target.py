class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #here we need to return all paths from 0 till n-1 and since its a dag there is no need of keeping a visited array
        res=[]
        ds=[]
        n=len(graph)
        self.dfs(0,n-1,[],res,graph)
        return res

    def dfs(self,source,dest,ds,res,graph):
        ds.append(source)
        if(source==dest):
            res.append(ds.copy())
        for neigh in graph[source]:
            self.dfs(neigh,dest,ds,res,graph)
        ds.pop()
       


    
        
