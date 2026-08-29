class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #we will use recursion+memo to solve this 
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.helper(m-1,n-1,m,n,dp)

    def helper(self,i,j,m,n,dp):
        #we will move from m-1,n-1 to 0,0
        if(i==0 and j==0):
            return 1
        if(i<0 or j<0):
            return 0
        if(dp[i][j]!=-1):
            return dp[i][j]
        up=self.helper(i-1,j,m,n,dp)
        left=self.helper(i,j-1,m,n,dp)
        dp[i][j]=(up+left)
        return dp[i][j]
        