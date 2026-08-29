class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
       #here we need to return the minimum no of operations to convert word1 word2
       m=len(word1)
       n=len(word2)
       dp=[[-1 for i in range(n+1)]for j in range(m+1)]
       return self.helper(m-1,n-1,word1,word2,m,n,dp)

    def helper(self,i,j,s1,s2,m,n,dp):
        #there are three options insert,delete and replace 
        if(i<0):
            return j+1
        if(j<0):
            return i+1
        if(dp[i][j]!=-1):
            return dp[i][j]
        
        if(s1[i]==s2[j]):
            dp[i][j]=self.helper(i-1,j-1,s1,s2,m,n,dp)
            return dp[i][j]
        else:
            #its basically insert at second and delete at first
            insert=self.helper(i,j-1,s1,s2,m,n,dp)
            delete=self.helper(i-1,j,s1,s2,m,n,dp)
            replace=self.helper(i-1,j-1,s1,s2,m,n,dp)
            dp[i][j]=1+min(insert,delete,replace)
            return dp[i][j]
