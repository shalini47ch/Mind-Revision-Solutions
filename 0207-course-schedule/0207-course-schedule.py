from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for i in range(numCourses)]
        for u,v in prerequisites:
            adj[v].append(u)
        indegree=[0 for i in range(numCourses)]
        for i in range(0,numCourses):
            for neigh in adj[i]:
                indegree[neigh]+=1
        queue=deque()
        #keep iterating while queue is empty
        for i in range(0,numCourses):
            if(indegree[i]==0):
                queue.append(i)
        ans=[]
        while(queue):
            node=queue.popleft()
            ans.append(node)
            for neigh in adj[node]:
                indegree[neigh]-=1
                if(indegree[neigh]==0):
                    queue.append(neigh)
        if(len(ans)==numCourses):
            return True
        return False



        