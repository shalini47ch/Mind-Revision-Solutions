from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #use toposort to solve this 
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        indegree=[0 for i in range(numCourses)]
        queue=deque()
        #first calcualte the indegree
        for i in range(0,numCourses):
            for neigh in adj[i]:
                indegree[neigh]+=1
        for i in range(0,numCourses):
            if(indegree[i]==0):
                queue.append(i)
        ans=[]
        #keep iterating while queue is empty
        while(queue):
            node=queue.popleft()
            ans.append(node)
            for neigh in adj[node]:
                indegree[neigh]-=1
                if(indegree[neigh]==0):
                    queue.append(neigh)
        if(len(ans)==numCourses):
            return ans
        return []
       