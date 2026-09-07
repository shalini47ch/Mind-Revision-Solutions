class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #so its basically with s we need to return the no of distinct subsequences of t 
        #use recursion+memo to solve this 
        m=len(s)
        n=len(t)
        dp=[[-1 for i in range(n+1)]for j in range(m+1)]
        return self.helper(m-1,n-1,s,t,dp)

    def helper(self,ind1,ind2,s,t,dp):
        if(ind2<0):
            return 1
        if(ind1<0):
            return 0
        if(dp[ind1][ind2]!=-1):
            return dp[ind1][ind2]
        #now if the characters are same there are two options either to pick or notpick
        if(s[ind1]==t[ind2]):
            ele1=self.helper(ind1-1,ind2-1,s,t,dp)
            ele2=self.helper(ind1-1,ind2,s,t,dp)
            dp[ind1][ind2]=(ele1+ele2)
            return dp[ind1][ind2]
        else:
            #this is the case when the characters are not equal
            dp[ind1][ind2]=self.helper(ind1-1,ind2,s,t,dp)
            return dp[ind1][ind2]

        