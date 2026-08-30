class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #use recursion+memo to solve this 
        n=len(s)
        dp=[-1 for i in range(n+1)]
        return self.helper(0,s,wordDict,n,dp)

    def helper(self,ind,s,wordDict,n,dp):
        if(ind==n):
            return True 
        if(dp[ind]!=-1):
            return dp[ind]
        for j in range(ind+1,n+1):
            if(s[ind:j] in wordDict and self.helper(j,s,wordDict,n,dp)):
                dp[ind]=True
                return dp[ind]
        dp[ind]=False
        return dp[ind]


       