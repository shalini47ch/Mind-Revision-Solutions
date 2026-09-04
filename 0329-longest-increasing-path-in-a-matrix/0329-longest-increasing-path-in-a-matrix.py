class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        #lets try to solve this using the concept of dfs 
        m=len(matrix)
        n=len(matrix[0])
        dirs=[(-1,0),(1,0),(0,-1),(0,1)]
        dp=[[0 for i in range(n)]for j in range(m)]
        def dfs(i,j):
            #lets find the longest increasing path here
            if(dp[i][j]!=0):
                return dp[i][j]
            best=1
            for dr,dc in dirs:
                nrow=i+dr
                ncol=j+dc
                #now the next step is to check for validity
                if(nrow>=0 and nrow<m and ncol>=0 and ncol<n and 
                matrix[nrow][ncol]>matrix[i][j]):
                    best=max(best,1+dfs(nrow,ncol))
            dp[i][j]=best
            return dp[i][j]
        #now at last we need to return the length of longest increasing path
        maxi=0
        for i in range(0,m):
            for j in range(0,n):
                maxi=max(maxi,dfs(i,j))
        return maxi

                   